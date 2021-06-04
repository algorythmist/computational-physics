import unittest

from qc.gates import *
from qc.qc import is_unit_matrix


class GatesTestCase(unittest.TestCase):

    def test_tofoli(self):
        t = tofoli()
        u = t @ t
        self.assertTrue(is_unit_matrix(u))

    def test_fredkin(self):
        f = fredkin()
        u = f @ f
        self.assertTrue(is_unit_matrix(u))

    def test_bit_bit_inner_product(self):
        self.assertEqual(0, bit_inner_product("000", "000"))
        self.assertEqual(1, bit_inner_product("01", "01"))
        self.assertEqual(1, bit_inner_product("111", "111"))
        self.assertEqual(0, bit_inner_product("110", "111"))

    def test_into_to_bits(self):
        self.assertEqual("0001", int_to_bits(1, 4))
        self.assertEqual("011", int_to_bits(3, 3))

    def test_hadamard(self):
        h = hadamard()
        self.assertAlmostEqual(0.70710678, h[0][1])
        self.assertAlmostEqual(-0.70710678, h[1][1])

        h = hadamard(2)
        self.assertAlmostEqual(0.5, h[0][1])
        self.assertAlmostEqual(-0.5, h[1][1])

