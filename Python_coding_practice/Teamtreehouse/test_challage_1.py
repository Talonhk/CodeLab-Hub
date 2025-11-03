import unittest
from datetime import datetime
from Challage_1 import parse_telemetry, check_violations

class TestTelemetryProcessing(unittest.TestCase):

    def test_parse_telemetry_valid(self):
        line = "20180101 23:01:05.001|1001|101|98|25|20|99.9|TSTAT"
        expected = {
            "timestamp": datetime.strptime("20180101 23:01:05.001", "%Y%m%d %H:%M:%S.%f"),
            "satellite_id": "1001",
            "red_high_limit": 101.0,
            "yellow_high_limit": 98.0,
            "yellow_low_limit": 25.0,
            "red_low_limit": 20.0,
            "raw_value": 99.9,
            "component": "TSTAT"
        }
        result = parse_telemetry(line)
        self.assertEqual(result["timestamp"], expected["timestamp"])
        self.assertEqual(result["satellite_id"], expected["satellite_id"])
        self.assertEqual(result["red_high_limit"], expected["red_high_limit"])

    def test_parse_telemetry_invalid(self):
        line = "invalid|data|line"
        result = parse_telemetry(line)
        self.assertIsNone(result)

    def test_check_violations(self):
        data = [
            {
                "timestamp": datetime.strptime("20180101 23:01:05.001", "%Y%m%d %H:%M:%S.%f"),
                "satellite_id": "1001",
                "red_high_limit": 101.0,
                "yellow_high_limit": 98.0,
                "yellow_low_limit": 25.0,
                "red_low_limit": 20.0,
                "raw_value": 102.0,
                "component": "TSTAT"
            },
            {
                "timestamp": datetime.strptime("20180101 23:02:05.001", "%Y%m%d %H:%M:%S.%f"),
                "satellite_id": "1001",
                "red_high_limit": 101.0,
                "yellow_high_limit": 98.0,
                "yellow_low_limit": 25.0,
                "red_low_limit": 20.0,
                "raw_value": 103.0,
                "component": "TSTAT"
            },
            {
                "timestamp": datetime.strptime("20180101 23:03:05.001", "%Y%m%d %H:%M:%S.%f"),
                "satellite_id": "1001",
                "red_high_limit": 101.0,
                "yellow_high_limit": 98.0,
                "yellow_low_limit": 25.0,
                "red_low_limit": 20.0,
                "raw_value": 104.0,
                "component": "TSTAT"
            }
        ]
        alerts = check_violations(data)
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["satelliteId"], "1001")
        self.assertEqual(alerts[0]["severity"], "RED HIGH")
        self.assertEqual(alerts[0]["component"], "TSTAT")

if __name__ == "__main__":
    unittest.main()