import unittest

from pdes import *


class PDETestCase(unittest.TestCase):

    def test_laplace_1d(self):
        u = solve_laplace_1d(constant=-5, u0=1, u1=2)
        print(u)
        self.assertEqual(22, len(u))

    def test_laplace_2d_square(self):
        u = solve_laplace_2d_square(ut=5, ub=-5, ul=3, ur = -1)
        self.assertEqual((102,102), u.shape)
