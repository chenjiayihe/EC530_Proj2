import pytest
import sys

sys.path.append("..")
from Modules import device


class TestDevice:
    def test_no_input_data(self):
        with pytest.raises(ValueError):
            device.add_data(1, None, "test.json")

    def test_empty_input_data(self):
        with pytest.raises(ValueError):
            device.add_data(1, {}, "test.json")

    test_data = {
        "patient_id": "1",
        "temp": "97",
        "pulse": "60",
        "blood_pressure": "110",
        "oxygen_level": "90",
        "weight": "130",
        "glucose_level": "100"
    }

    def test_no_input_id(self):
        test_data = {
            "patient_id": "1",
            "temp": "97",
            "pulse": "60",
            "oxygen_level": "90",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(TypeError):
            device.add_data(test_data, "test.json")

    def test_no_output_file(self):
        test_data = {
            "patient_id": "1",
            "temp": "97",
            "pulse": "60",
            "oxygen_level": "90",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(TypeError):
            device.add_data(1, test_data)

    def test_invalid_userid(self):
        test_data = {
            "patient_id": "1000",
            "temp": "97",
            "pulse": "60",
            "oxygen_level": "90",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(KeyError):
            device.add_data(1000, test_data, "test.json")

    def test_invalid_input(self):
        test_data = {
            "patient_id": "1",
            "temp": "97",
            "pulse": "-1",
            "oxygen_level": "90",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(ValueError):
            device.add_data(1, test_data, "test.json")

    def test_invalid_input_type(self):
        test_data = {
            "patient_id": "1",
            "temp": "97",
            "pulse": "60",
            "blood_type": "333",
            "oxygen_level": "90",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(ValueError):
            device.add_data(1, test_data, "test.json")

    def test_invalid_input_range(self):
        test_data = {
            "patient_id": "1",
            "temp": "97",
            "pulse": "60",
            "blood_pressure": "110",
            "oxygen_level": "2000",
            "weight": "130",
            "glucose_level": "100"
        }
        with pytest.raises(ValueError):
            device.add_data(1, test_data, "test.json")
