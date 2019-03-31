# https://cp-algorithms.com/algebra/binary-exp.html
# O(logn) complexity algo to calculate the value of a^b
import unittest


def recursive_binary_exponentiation(a, b):
    if b < 0:
        raise Exception('Value Error')
    if b == 0:
        return 1
    res = recursive_binary_exponentiation(a, b // 2)
    if b % 2 == 1:
        return res * res * a
    else:
        return res * res


def iterative_binary_exponentiation(a, b):
    if b < 0:
        raise Exception('Value Error')
    res = 1
    while b > 0:
        if b & 1:
            res = res * a
        a = a * a
        b >>= 1
    return res


def big_number_mod(a, b, c):
    if b < 0:
        raise Exception('Value Error')
    elif c == 1:
        return 0
    a %= c
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % c
        a = a * a % c
        b >>= 1
    return res


class TestBE(unittest.TestCase):
    def test_recursive(self):
        self.assertEqual(recursive_binary_exponentiation(2, 4), 16)
        self.assertEqual(recursive_binary_exponentiation(2, 10), 1024)
        self.assertEqual(recursive_binary_exponentiation(
            2, 99), 6.338253001141147e+29)
        self.assertEqual(recursive_binary_exponentiation(2, 0), 1)
        self.assertEqual(recursive_binary_exponentiation(2, 1), 2)
        with self.assertRaises(Exception) as context:
            recursive_binary_exponentiation(2, -1)
        self.assertTrue(str(context.exception), 'Value Error')

    def test_iterative(self):
        self.assertEqual(iterative_binary_exponentiation(2, 4), 16)
        self.assertEqual(iterative_binary_exponentiation(2, 10), 1024)
        self.assertEqual(iterative_binary_exponentiation(
            2, 99), 6.338253001141147e+29)
        self.assertEqual(iterative_binary_exponentiation(2, 0), 1)
        self.assertEqual(iterative_binary_exponentiation(2, 1), 2)
        with self.assertRaises(Exception) as context:
            iterative_binary_exponentiation(2, -1)
        self.assertTrue(str(context.exception), 'Value Error')

    def test_mod(self):
        self.assertEqual(big_number_mod(2, 0, 1), 0)
        self.assertEqual(big_number_mod(2, 2147483647, 13), 11)
