import unittest
from app.square import Square
from app.math import Math
from parameterized import parameterized


class TestSquare(unittest.TestCase):
    def setUp(self):
        side = 2
        math_util = Math()
        self._square = Square(side, math_util)

    def test_area(self):
        expected = 4
        result = self._square.area()
        self.assertEqual(expected, result)

    def test_circumference(self):
        expected = 8
        result = self._square.circumference()
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("side = 0", Square(0, Math()), 0),
        ("side = 1", Square(1, Math()), 1),
        ("side = 99", Square(99, Math()), 9801),
    ])
    def test_area_parameterized(self, name, square, expected):
        self._square = square
        result = self._square.area()
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("side = 0", Square(0, Math()), 0),
        ("side = 1", Square(1, Math()), 4),
        ("side = 99", Square(99, Math()), 396),
    ])
    def test_circumference_parameterized(self, name, square, expected):
        self._square = square
        result = self._square.circumference()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
