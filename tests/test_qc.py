import unittest

from qc.qc import *
from qc.gates import *


class QCTestCase(unittest.TestCase):

    def test_outer_vector_product(self):
        x = vector([2, 3])
        y = vector([4, 6, 3])
        t = outer_product(x, y)
        self.assertEqual("[ 8 12  6 12 18  9]", str(t.ravel()))

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



