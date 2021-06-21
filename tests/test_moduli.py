import unittest

from qc.moduli import *


class NumbersTestCase(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(3, gcd(21,15))
        self.assertEqual(3, gcd(9, 15))
        self.assertEqual(3, gcd(9, 3))
        self.assertEqual(1, gcd(9, 28))

    def test_find_comprime(self):
        coprime = find_coprime(15)
        self.assertEqual(1, gcd(coprime, 15))

    def test_powers(self):
        p = powers(2, 15)
        self.assertEqual('[2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8, 1, 2]', str(p))
        p = powers(13, 15)
        self.assertEqual('[13, 4, 7, 1, 13, 4, 7, 1, 13, 4, 7, 1, 13]', str(p))

    def test_find_period(self):
        period = find_period(2, 371)
        self.assertEqual(156, period)
        self.assertEqual(78, find_period(24, 371))
