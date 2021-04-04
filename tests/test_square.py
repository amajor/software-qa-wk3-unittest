import unittest
from app.square import Square
from unittest.mock import MagicMock


class TestSquare(unittest.TestCase):
    def setUp(self):
        # Set up mocks
        self._math_mock = MagicMock()
        self._math_mock.power = MagicMock(return_value=25)
        self._math_mock.add = MagicMock(return_value=20)

        # Set up Square()
        default_side = 5
        self._square = Square(default_side, self._math_mock)

    def test_area(self):
        expected = 25
        result = self._square.area()
        self.assertEqual(expected, result)

    def test_circumference(self):
        expected = 20
        result = self._square.circumference()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
