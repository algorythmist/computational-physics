import unittest

from qc import *


class QCTestCase(unittest.TestCase):

    def test_outer_vector_product(self):
        x = vector([2, 3])
        y = vector([4, 6, 3])
        t = outer_product(x, y)
        self.assertEqual("[ 8 12  6 12 18  9]", str(t.ravel()))

    def test_qubits_to_vector(self):
        v = qubits_to_vector("011")
        self.assertEqual("[0 0 0 1 0 0 0 0]", str(v))
        v = qubits_to_vector("111")
        self.assertEqual("[0 0 0 0 0 0 0 1]", str(v))

    def test_tofoli(self):
        t = tofoli()
        u = t @ t
        self.is_unit_matrix(u)

    def test_fredkin(self):
        f = fredkin()
        u = f @ f
        self.is_unit_matrix(u)

    def test_state_from_bloch(self):
        theta = np.pi / 4
        phi = np.pi / 4
        s = state_from_bloch(theta, phi)
        self.assertEqual("[0.70710678+0.j  0.5       +0.5j]", str(s))

    def is_unit_matrix(self, u):
        for i, j in np.ndindex(u.shape):
            if i == j:
                self.assertEqual(1., u[i, j])
            else:
                self.assertEqual(0., u[i, j])
