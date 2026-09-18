import sys
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict, deque

# Constants for configuration
VALID_COMPONENTS = {"battery", "thermostat"}
COMPONENT_LABELS = {"battery": "BATT", "thermostat": "TSTAT"}
TIME_WINDOW_MINUTES = 5

def configure_logging(debug=False):
    """Configure logging level and format."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def parse_telemetry(line):
    """Parse a single line of telemetry data into a dictionary."""
    try:
        parts = line.strip().split('|')
        timestamp = datetime.strptime(parts[0], "%Y%m%d %H:%M:%S.%f")
        timestamp = timestamp.replace(microsecond=(timestamp.microsecond // 1000) * 1000)
        return {
            "timestamp": timestamp,
            "satellite_id": parts[1],
            "red_high_limit": float(parts[2]),
            "yellow_high_limit": float(parts[3]),
            "yellow_low_limit": float(parts[4]),
            "red_low_limit": float(parts[5]),
            "raw_value": float(parts[6]),
            "component": parts[7]
        }
    except (ValueError, IndexError) as e:
        logging.error(f"Failed to parse line: {line.strip()} | Error: {e.__class__.__name__}: {e}")
        return None
    except Exception as e:
        logging.exception(f"Unexpected error parsing line: {line.strip()}")
        return None

def deduplicate_lines(lines):
    """Yield unique lines based on their hash to avoid duplicates."""
    seen = set()
    for line in lines:
        line_hash = hash(line.strip())
        if line_hash not in seen:
            seen.add(line_hash)
            yield line

def filter_and_parse(lines):
    """Parse lines and yield valid telemetry entries with known components."""
    for line in lines:
        if not line.strip():
            continue
        data = parse_telemetry(line)
        if data and data["component"] in VALID_COMPONENTS:
            yield data

def format_timestamp(dt):
    """Format a datetime object to ISO 8601 with millisecond precision and 'Z' suffix."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def check_violations(parsed_entries):
    """Check for RED LOW and RED HIGH violations and generate alerts."""
    battery_violations = defaultdict(deque)
    thermostat_violations = defaultdict(deque)
    alerts = []
    for entry in sorted(parsed_entries, key=lambda x: x["timestamp"]):
        timestamp = entry["timestamp"]
        satellite_id = entry["satellite_id"]
        component = entry["component"]
        raw_value = entry["raw_value"]
        red_high_limit = entry["red_high_limit"]
        red_low_limit = entry["red_low_limit"]

        if component == "battery" and raw_value < red_low_limit:
            dq = battery_violations[satellite_id]
            dq.append(timestamp)
            while dq and (timestamp - dq[0]) > timedelta(minutes=TIME_WINDOW_MINUTES):
                dq.popleft()
            if len(dq) == 3:
                alerts.append({
                    "satelliteId": satellite_id,
                    "severity": "RED LOW",
                    "component": COMPONENT_LABELS[component],
                    "timestamp": format_timestamp(dq[0])
                })
                dq.clear()
        elif component == "thermostat" and raw_value > red_high_limit:
            dq = thermostat_violations[satellite_id]
            dq.append(timestamp)
            while dq and (timestamp - dq[0]) > timedelta(minutes=TIME_WINDOW_MINUTES):
                dq.popleft()
            if len(dq) == 3:
                alerts.append({
                    "satelliteId": satellite_id,
                    "severity": "RED HIGH",
                    "component": COMPONENT_LABELS[component],
                    "timestamp": format_timestamp(dq[0])
                })
                dq.clear()
    return alerts

def process_telemetry(file_path, debug=False):
    """Main function to process telemetry data from a file and return alerts as JSON."""
    configure_logging(debug)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        deduped = deduplicate_lines(lines)
        parsed = list(filter_and_parse(deduped))
        alerts = check_violations(parsed)
        return json.dumps(alerts, indent=4)
    except FileNotFoundError:
        logging.error(f"Error: File not found - {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.exception(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    debug = "--debug" in sys.argv
    if debug:
        sys.argv.remove("--debug")
    if len(sys.argv) != 2:
        print("Usage: python Challenge_1.py <file_path> [--debug]")
        sys.exit(1)
    file_path = sys.argv[1]
    output = process_telemetry(file_path, debug)
    print(output)
