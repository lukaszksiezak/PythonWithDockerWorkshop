import unittest

from EnvironmentalSensorProcessor import (
    POOR_CONDITIONS, TOLERABLE_CONDITIONS, GOOD_CONDITIONS,
    process_environment, dict_to_series, TIMESTAMP, VALUE)

class TestSensor(unittest.TestCase):
    """
    Tests for EnvrionmentalSensor module
    """

    def test_process_environment_should_be_poor(self):
        """
        Unit tests for process_environment method.
        Test cases for poor conditions
        """
        # Arrange:
        high_temperature, high_humidity = self._prepare_test_series(
            temperature_values=[70, 76, 66], humidity_values=[90, 89, 91]
        )
        # Act:
        kpi = process_environment(high_temperature, high_humidity)
        # Assert:
        self.assertEquals(kpi, POOR_CONDITIONS)

    def test_process_environment_should_be_torelable(self):
        """
        Unit tests for process_environment method.
        Test cases for torelable conditions
        """
        # Arrange:
        temperature, humidity = self._prepare_test_series(
            temperature_values=[2, 12, 11], humidity_values=[44, 41, 45]
        )
        # Act:
        kpi = process_environment(temperature, humidity)
        # Assert:
        self.assertEquals(kpi, TOLERABLE_CONDITIONS)

    def test_process_environment_should_be_good(self):
        """
        Unit tests for process_environment method.
        Test cases for good conditions
        """
        # Arrange:
        temperature, humidity = self._prepare_test_series(
            temperature_values=[25, 27, 38], humidity_values=[20, 21, 25]
        )
        # Act:
        kpi = process_environment(temperature, humidity)
        # Assert:
        self.assertEquals(kpi, GOOD_CONDITIONS)

    def _prepare_test_series(self, temperature_values:list, humidity_values:list) -> tuple:
        """
        For given list of values (temperature and humidity) (floats)
        generate tuple of to series (temperature, humidity) -
        ready to use inputs for process_environment method
        """
        temperature = {
            TIMESTAMP: [
                "2020-10-10 00:03:09.518",
                "2020-10-10 00:03:48.151",
                "2020-10-10 00:04:25.012",
            ],
            VALUE: temperature_values
        }
        humidity = {
            TIMESTAMP: [
                "2020-10-10 00:03:09.518",
                "2020-10-10 00:03:48.151",
                "2020-10-10 00:04:25.012",
            ],
            VALUE: humidity_values
        }

        temperature = dict_to_series(temperature)
        humidity = dict_to_series(humidity)

        return temperature, humidity