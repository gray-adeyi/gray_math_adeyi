from unittest import TestCase
from .main import power, factorial, combination, permutation


class PackageTestCase(TestCase):
    def test_power(self):
        test_values = [
            ((2, 3), 8),
            ((3, 2), 9),
            ((5, 3), 125),
        ]
        for value in test_values:
            with self.subTest():
                result = power(*value[0])
                self.assertEqual(result, value[1])

    def test_factorial(self):
        test_values = [
            (3, 6),
            (5, 120),
            (4, 24),
        ]
        for values in test_values:
            with self.subTest():
                result = factorial(values[0])
                self.assertEqual(result, values[1])
