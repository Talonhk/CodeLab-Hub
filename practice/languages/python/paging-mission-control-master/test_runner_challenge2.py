import subprocess
import tempfile
import json
import os
import logging
import sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)

# Define your test cases
TEST_CASES = [
    {
        "name": "Battery RED LOW Violation",
        "input": """20240516 12:00:00.000|1|4.2|4.1|3.9|3.8|3.7|BATT
20240516 12:01:00.000|1|4.2|4.1|3.9|3.8|3.6|BATT
20240516 12:02:00.000|1|4.2|4.1|3.9|3.8|3.5|BATT
""",
        "expected": [
            {
                "satelliteId": 1,
                "severity": "RED LOW",
                "component": "BATT",
                "timestamp": "2024-05-16T12:00:00.000Z"
            }
        ]
    },
    {
        "name": "Thermostat RED HIGH Violation",
        "input": """20240516 13:00:00.000|2|80.0|75.0|65.0|60.0|81.0|TSTAT
20240516 13:01:00.000|2|80.0|75.0|65.0|60.0|82.0|TSTAT
20240516 13:02:00.000|2|80.0|75.0|65.0|60.0|83.0|TSTAT
""",
        "expected": [
            {
                "satelliteId": 2,
                "severity": "RED HIGH",
                "component": "TSTAT",
                "timestamp": "2024-05-16T13:00:00.000Z"
            }
        ]
    },
    {
        "name": "Malformed Line",
        "input": "20240516 15:00:00.000|4|4.2|4.1|3.9|3.8|3.7\n",
        "expected": []
    },
    {
        "name": "Unknown Component",
        "input": "20240516 16:00:00.000|5|4.2|4.1|3.9|3.8|3.7|SOLAR\n",
        "expected": []
    },
    {
        "name": "No Violation",
        "input": """20240516 17:00:00.000|6|4.2|4.1|3.9|3.8|4.0|BATT
20240516 17:01:00.000|6|4.2|4.1|3.9|3.8|4.1|BATT
20240516 17:02:00.000|6|4.2|4.1|3.9|3.8|4.2|BATT
""",
        "expected": []
    }
]

def run_test_case(script_path, test_case):
    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        tmp.write(test_case["input"])
        tmp.flush()
        tmp_name = tmp.name

    try:
        result = subprocess.run(
            ["python3", script_path, tmp_name],
            capture_output=True, text=True, timeout=10
        )
        try:
            output = json.loads(result.stdout.strip())
        except Exception:
            print("Raw output:", result.stdout)
            output = None

        passed = output == test_case["expected"]
        print(f"Test: {test_case['name']}: {'PASS' if passed else 'FAIL'}")
        if not passed:
            print("Expected:", json.dumps(test_case["expected"], indent=2))
            print("Got     :", result.stdout.strip())
    finally:
        os.unlink(tmp_name)

if __name__ == "__main__":
    script_path = "Challenge_2.py"
    for test_case in TEST_CASES:
        run_test_case(script_path, test_case)