import unittest
from app.weather_client import WeatherClient
from parameterized import parameterized
from unittest.mock import patch


class TestWeatherClient(unittest.TestCase):
    SAMPLE_RESPONSE = b'{ "weather": [{ "description": "sunny here!" }]}'
    RESPONSE_SUNNY = b'{ "weather": [{ "description": "sunny all day" }]}'
    RESPONSE_COLD = b'{ "weather": [{ "description": "it might snow" }]}'
    RESPONSE_RAIN = b'{ "weather": [{ "description": "light rain expected" }]}'

    def setUp(self):
        # Set up weather client
        self._weather = WeatherClient()

    # Patch in the response that "requests" module would return
    @patch('requests.get')
    def test_get_weather_by_zip(self, mock_requests, sample_response=SAMPLE_RESPONSE):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.content = sample_response

        zipcode = "49464"
        expected = "sunny here!"
        result = self._weather.get_weather_by_zip(zipcode)
        self.assertEqual(expected, result)

    # Patch in the response that "requests" module would return
    @patch('requests.get')
    def test_get_weather_by_zip_raise_error(self, mock_requests):
        mock_requests.return_value.status_code = 401
        """Test case: non-200 status raises exception"""
        with self.assertRaises(Exception):
            self._weather.get_weather_by_zip("00000")

    # Parameterize for additional testing scenarios
    @parameterized.expand([
        ("Zeeland, MI", "49464", RESPONSE_RAIN, "light rain expected"),
        ("Houston, TX", "77077", RESPONSE_SUNNY, "sunny all day"),
        ("Anchorage, AK", "99501", RESPONSE_COLD, "it might snow")
    ])
    @patch('requests.get')
    def test_get_weather_by_zip(self, name, zipcode, sample_response, expected, mock_requests):
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.content = sample_response

        result = self._weather.get_weather_by_zip(zipcode)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
