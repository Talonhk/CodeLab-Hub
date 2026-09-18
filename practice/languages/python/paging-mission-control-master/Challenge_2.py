import sys
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict, deque

# --- Configuration ---

# Acceptable canonical component names
VALID_COMPONENTS = {"BATT", "TSTAT"}
# Time window in minutes for violation detection
TIME_WINDOW_MINUTES = 5

def configure_logging(debug=False):
    """Configure logging level and format."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def parse_line(line):
    """
    Parse a single line of telemetry data into a dictionary.
    Returns None if the line is malformed or cannot be parsed.
    """
    try:
        parts = line.strip().split('|')
        timestamp = datetime.strptime(parts[0], "%Y%m%d %H:%M:%S.%f")
        # Normalize timestamp to millisecond precision
        timestamp = timestamp.replace(microsecond=(timestamp.microsecond // 1000) * 1000)
        return {
            "timestamp": timestamp,
            "satellite_id": int(parts[1]),
            "red_high": float(parts[2]),
            "yellow_high": float(parts[3]),
            "yellow_low": float(parts[4]),
            "red_low": float(parts[5]),
            "raw_value": float(parts[6]),
            "component": parts[7].strip().upper()  # Normalize to uppercase for consistency
        }
    except (ValueError, IndexError) as e:
        logging.error(f"Failed to parse line: {line.strip()} | Error: {e.__class__.__name__}: {e}")
        return None
    except Exception as e:
        logging.exception(f"Unexpected error parsing line: {line.strip()}")
        return None

def deduplicate_lines(lines):
    """
    Yield unique lines based on their hash to avoid duplicates.
    Strips whitespace before hashing.
    """
    seen = set()
    for line in lines:
        line_hash = hash(line.strip())
        if line_hash not in seen:
            seen.add(line_hash)
            yield line

def filter_and_parse(lines):
    """
    Parse lines and yield valid telemetry entries with known components.
    Skips empty lines and lines with unknown components.
    """
    for line in lines:
        if not line.strip():
            continue
        data = parse_line(line)
        if data and data["component"] in VALID_COMPONENTS:
            yield data

def format_timestamp(dt):
    """
    Format a datetime object to ISO 8601 with millisecond precision and 'Z' suffix.
    Example: 2024-05-16T12:34:56.789Z
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def check_violations(parsed_entries):
    """
    Check for RED LOW and RED HIGH violations and generate alerts.
    - RED LOW: 3 battery readings below red_low within 5 minutes.
    - RED HIGH: 3 thermostat readings above red_high within 5 minutes.
    """
    batt_violations = defaultdict(deque)   # Battery violation timestamps per satellite
    tstat_violations = defaultdict(deque)  # Thermostat violation timestamps per satellite
    alerts = []
    for data in sorted(parsed_entries, key=lambda x: x["timestamp"]):
        ts = data["timestamp"]
        sat = data["satellite_id"]
        comp = data["component"]
        val = data["raw_value"]
        red_high = data["red_high"]
        red_low = data["red_low"]

        if comp == "BATT" and val < red_low:
            dq = batt_violations[sat]
            dq.append(ts)
            # Remove timestamps outside the time window
            while dq and (ts - dq[0]) > timedelta(minutes=TIME_WINDOW_MINUTES):
                dq.popleft()
            # Trigger alert if 3 violations in window
            if len(dq) == 3:
                alerts.append({
                    "satelliteId": sat,
                    "severity": "RED LOW",
                    "component": comp,
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
                    "component": comp,
                    "timestamp": format_timestamp(dq[0])
                })
                dq.clear()
    return alerts

def process_telemetry(filename):
    """
    Main function to process telemetry data from a file and return alerts.
    Steps:
    - Read file
    - Deduplicate lines
    - Parse and filter lines
    - Check for violations
    """
    if ".." in filename or "/" in filename or "\\" in filename:
        logging.error("Invalid filename: path traversal detected.")
        sys.exit(1)
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        deduped = deduplicate_lines(lines)
        parsed = list(filter_and_parse(deduped))
        return check_violations(parsed)
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        sys.exit(1)
    except Exception as e:
        logging.exception(f"Error processing telemetry: {e}")
        return []

if __name__ == "__main__":
    # Enable debug logging if '--debug' is passed
    debug = "--debug" in sys.argv
    if debug:
        sys.argv.remove("--debug")
    configure_logging(debug)
    if len(sys.argv) != 2:
        print("Usage: python Challenge_2.py <input_file> [--debug]")
        sys.exit(1)
    alerts = process_telemetry(sys.argv[1])
    print(json.dumps(alerts, indent=4))