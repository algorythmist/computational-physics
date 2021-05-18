import unittest

from geometry import *


class GeometryTestCase(unittest.TestCase):

    def test_metric(self):
        D = hyperbolic_metric(3)
        print(D)
        self.assertEqual(-1, D[2, 2])

    def test_normalize_spherical(self):
        p = [1, 0, 1]
        np = normalize_spherical(p)
        self.assertAlmostEqual(0.70710678, np[0], 5)

    def test_hyperbolic(self):
        p = [2, 1, 3]
        q = [1, 2, 1]
        hi = hyperbolic_inner(p, q)
        self.assertEqual(1, hi)
        try:
            normalize_hyperbolic(q)
            self.fail("Should have raised error")
        except ValueError:
            pass
        np = normalize_hyperbolic(p)
        self.assertEqual(0.75, np[-1])

