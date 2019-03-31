# https://cp-algorithms.com/algebra/euclid-algorithm.html
# Calculates GCD of two numbers in O(log min(a, b))
import unittest


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a / gcd(a, b) * b


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(55, 33), 11)

    def test_lcm(self):
        self.assertEqual(lcm(10, 1), 10)
        self.assertEqual(lcm(512, 124325234), 31827259904)
