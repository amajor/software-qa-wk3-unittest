import unittest
from parameterized import parameterized
from app.math import Math


class TestMath(unittest.TestCase):
    def setUp(self):
        self._math = Math()

    @parameterized.expand([
        ("two positive integers", 10, 20, 30),
        ("two negative integers", -10, -20, -30),
        ("mixed integers", 10, -4, 6),
        ("positive integer and zero", 7, 0, 7)
    ])
    def test_add(self, name, int1, int2, expected):
        result = self._math.add(int1, int2)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("two positive integers", 10, 20, 200),
        ("two negative integers", -10, -20, 200),
        ("mixed integers", 10, -4, -40),
        ("positive integer and zero", 7, 0, 0)
    ])
    def test_multiply(self, name, int1, int2, expected):
        result = self._math.multiply(int1, int2)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("two positive integers", 10, 20, 0.5),
        ("two negative integers", -10, -20, 0.5),
        ("mixed integers", 10, -4, -2.5),
        ("zero and positive integer", 0, 7, 0)
    ])
    def test_divide(self, name, int1, int2, expected):
        result = self._math.divide(int1, int2)
        self.assertEqual(expected, result)

    def test_divide_by_zero(self):
        """Test case: 10 divided by 0 raises ValueError"""
        with self.assertRaises(ValueError):
            self._math.divide(7, 0)

    @parameterized.expand([
        ("an even integer", 10, True),
        ("an odd integer", 5, False),
        ("a negative even integer", -4, True),
        ("a negative odd integer", -7, False),
        ("zero", 0, True)
    ])
    def test_is_even(self, name, int1, expected):
        result = self._math.is_even(int1)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("5 to the power of 1", 5, 1, 5),
        ("5 to the power of 5", 5, 5, 3125)
    ])
    def test_power(self, name, base, power, expected):
        result = self._math.power(base, power)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ("zero", 0, False),
        ("a prime number", 1, True),
        ("a prime number", 2, True),
        ("a prime number", 3, True),
        ("a prime number", 5, True),
        ("a prime number", 7, True),
        ("a large prime number", 7919, True),
        ("an even number", 4, False),
        ("large number divisible by 3", 999999, False)
    ])
    def test_is_prime(self, name, number, expected):
        result = self._math.is_prime(number)
        self.assertEqual(expected, result)

    def test_is_prime_negative_numbers(self):
        """Test case: -3 raises ValueError"""
        with self.assertRaises(ValueError):
            self._math.is_prime(-3)

    @parameterized.expand([
        ("zero", 0, 1),
        ("one", 1, 1),
        ("positive integer", 9, 362880)
    ])
    def test_factorial(self, name, number, expected):
        result = self._math.factorial(number)
        self.assertEqual(expected, result)

    def test_factorial_negative_numbers(self):
        """Test case: -8 raises ValueError"""
        with self.assertRaises(ValueError):
            self._math.factorial(-8)

    @parameterized.expand([
        ("one", 1, [1]),
        ("two", 2, [1, 2]),
        ("three", 3, [1, 3]),
        ("positive integer (8)", 8, [1, 8, 2, 4]),
        ("positive integer (20)", 20, [1, 20, 2, 4, 5, 10])
    ])
    def test_factors(self, name, number, expected):
        result = self._math.factors(number)
        self.assertListEqual(expected, result)

    def test_factors_negative_numbers(self):
        """Test case: -9 raises ValueError"""
        with self.assertRaises(ValueError):
            self._math.factors(-9)

    def test_factors_zero(self):
        """Test case: 0 raises ValueError"""
        with self.assertRaises(ValueError):
            self._math.factors(0)

if __name__ == '__main__':
    unittest.main()
