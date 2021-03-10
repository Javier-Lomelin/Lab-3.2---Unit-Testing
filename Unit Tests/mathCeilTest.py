import unittest
import math


class MathCeilTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(math.ceil(75.87), 76)

    def test_near_zero(self):
        self.assertEqual(math.ceil(0.01), 1)
        self.assertEqual(math.ceil(-0.01), 0)

    def test_zero(self):
        self.assertEqual(math.ceil(0.0), 0)

    def test_negative(self):
        self.assertEqual(math.ceil(-45.67), -45)
