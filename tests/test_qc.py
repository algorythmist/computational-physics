import unittest

from qc.gates import *
from qc.qc import *


class QCTestCase(unittest.TestCase):

    def test_vector_outer_product(self):
        x = vector([2, 3])
        y = vector([4, 6, 3])
        t = outer_product(x, y)
        self.assertEqual("[ 8 12  6 12 18  9]", str(t.ravel()))

    def test_gate_outer_product(self):
        product = outer_product(NOT, identity(2))
        self.assertEqual('[[0. 0. 1. 0.]\n' \
                         ' [0. 0. 0. 1.]\n' \
                         ' [1. 0. 0. 0.]\n' \
                         ' [0. 1. 0. 0.]]', str(product))

    def test_create_bell_state(self):
        """
        Build a bell state by applying two sets of gates to a 2-bit system
        :return:
        """
        gate1 = outer_product(hadamard(), identity(2))
        gate2 = CNOT
        input = bits_to_vector("00")
        output1 = gate1 @ input
        output2 = gate2 @ output1
        self.assertAlmostEqual(0.70710678, output2[0])
        self.assertEqual(0, output2[1])
        self.assertEqual(0, output2[2])
        self.assertAlmostEqual(0.70710678, output2[3])

    def test_bits_to_vector(self):
        v = bits_to_vector("011")
        self.assertEqual(3, bits_to_int("011"))
        self.assertEqual("[0 0 0 1 0 0 0 0]", str(v))
        v = bits_to_vector("111")
        self.assertEqual(7, bits_to_int("111"))
        self.assertEqual("[0 0 0 0 0 0 0 1]", str(v))

    def test_state_from_bloch(self):
        theta = np.pi / 4
        phi = np.pi / 4
        s = state_from_bloch(theta, phi)
        self.assertEqual("[0.70710678+0.j  0.5       +0.5j]", str(s))
