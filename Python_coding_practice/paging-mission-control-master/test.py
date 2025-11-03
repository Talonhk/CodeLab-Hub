import sys
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict, deque

# Canonical component mapping
COMPONENT_ALIASES = {
    "battery": "BATT",
    "batt": "BATT",
    "thermostat": "TSTAT",
    "tstat": "TSTAT"
}
TIME_WINDOW_MINUTES = 5

def configure_logging(debug=False):
    """Set up logging."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")

def normalize_component(name):
    """Return canonical component name or None if unknown."""
    return COMPONENT_ALIASES.get(name.strip().lower())

def parse_telemetry(line):
    """Parse a telemetry line into a dict, or None if invalid."""
    try:
        parts = line.strip().split('|')
        if len(parts) < 8:
            logging.error(f"Malformed line (not enough fields): {line.strip()}")
            return None
        timestamp = datetime.strptime(parts[0], "%Y%m%d %H:%M:%S.%f")
        timestamp = timestamp.replace(microsecond=(timestamp.microsecond // 1000) * 1000)
        component = normalize_component(parts[7])
        if not component:
            logging.warning(f"Unknown component '{parts[7]}' in line: {line.strip()}")
            return None
        return {
            "timestamp": timestamp,
            "satellite_id": parts[1].strip(),
            "red_high_limit": float(parts[2]),
            "yellow_high_limit": float(parts[3]),
            "yellow_low_limit": float(parts[4]),
            "red_low_limit": float(parts[5]),
            "raw_value": float(parts[6]),
            "component": component
        }
    except (ValueError, IndexError) as e:
        logging.error(f"Failed to parse line: {line.strip()} | Error: {e}")
        return None
    except Exception as e:
        logging.exception(f"Unexpected error parsing line: {line.strip()}")
        return None

def deduplicate_lines(lines):
    """Yield unique lines by content hash."""
    seen = set()
    for line in lines:
        key = hash(line.strip())
        if key not in seen:
            seen.add(key)
            yield line

def filter_and_parse(lines):
    """Yield valid, parsed telemetry entries."""
    for line in lines:
        if not line.strip():
            continue
        data = parse_telemetry(line)
        if data:
            yield data

def format_timestamp(dt):
    """Format datetime to ISO 8601 with ms and Z."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def check_violations(parsed_entries):
    """Generate alerts for RED LOW and RED HIGH violations."""
    batt_violations = defaultdict(deque)
    tstat_violations = defaultdict(deque)
    alerts = []
    for entry in sorted(parsed_entries, key=lambda x: x["timestamp"]):
        ts = entry["timestamp"]
        sat = entry["satellite_id"]
        comp = entry["component"]
        val = entry["raw_value"]
        red_high = entry["red_high_limit"]
        red_low = entry["red_low_limit"]

        if comp == "BATT" and val < red_low:
            dq = batt_violations[sat]
            dq.append(ts)
            while dq and (ts - dq[0]) > timedelta(minutes=TIME_WINDOW_MINUTES):
                dq.popleft()
            if len(dq) == 3:
                alerts.append({
                    "satelliteId": sat,
                    "severity": "RED LOW",
                    "component": "BATT",
                    "timestamp": format_timestamp(dq[0])
                })
                dq.clear()
        elif comp == "TSTAT" and val > red_high:
            dq = tstat_violations[sat]
            dq.append(ts)
            while dq and (ts - dq[0]) > timedelta(minutes=TIME_WINDOW_MINUTES):
                dq.popleft()
            if len(dq) == 3:
                alerts.append({
                    "satelliteId": sat,
                    "severity": "RED HIGH",
                    "component": "TSTAT",
                    "timestamp": format_timestamp(dq[0])
                })
                dq.clear()
    return alerts

def process_telemetry(filename, debug=False):
    """Read, parse, deduplicate, and check violations from file."""
    configure_logging(debug)
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        deduped = deduplicate_lines(lines)
        parsed = list(filter_and_parse(deduped))
        return check_violations(parsed)
    except FileNotFoundError:
        logging.error(f"Error: File not found - {filename}")
        sys.exit(1)
    except Exception as e:
        logging.exception(f"Error processing file: {e}")
        return []

if __name__ == "__main__":
    debug = "--debug" in sys.argv
    if debug:
        sys.argv.remove("--debug")
    configure_logging(debug)
    if len(sys.argv) != 2:
        print("Usage: python test.py <input_file> [--debug]")
        sys.exit(1)
    alerts = process_telemetry(sys.argv[1])
    print(json.dumps(alerts, indent=4))