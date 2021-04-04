import unittest
from app.weather_client import WeatherClient
from unittest.mock import patch


class TestWeatherClient(unittest.TestCase):
    SAMPLE_RESPONSE = b'{ "weather": [{ "description": "sunny here!" }]}'

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

if __name__ == '__main__':
    unittest.main()
