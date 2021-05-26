import unittest

from qc import *


class QCProblemsTestCase(unittest.TestCase):

    def test_problem_2_7_1(self):
        x = vector([3, 4, 7])
        y = vector([-1, 2])
        t = outer_product(x, y)
        self.assertEqual("[-3  6 -4  8 -7 14]", str(t.ravel()))

    def test_problem_2_7_3(self):
        m1 = [
            [3 + 2j, 5 - 1j, 2j],
            [0, 12, 6 - 3j],
            [2, 4 + 4j, 9 + 3j]
        ]
        m2 = [
            [1, 3 + 4j, 5 - 7j],
            [10 + 2j, 6, 2 + 5j],
            [0, 1, 2 + 9j]
        ]

        t = outer_product(m1, m2)
        print(t)  # TODO

    def test_problem_2_7_5(self):
        A = [[1, 2], [0, 1]]
        B = [[3, 2], [-1, 0]]
        C = [[6, 5], [3, 2]]
        BC = outer_product(B, C)
        ABC1 = outer_product(A, BC)
        AB = outer_product(A, B)
        ABC2 = outer_product(AB, C)
        self.assertTrue(np.array_equal(ABC1, ABC2))

    def test_problem_2_7_7(self):
        A = np.array([[2, 3]])
        B = np.array([[1, 2], [3, 4]])
        AB = outer_product(A, B)
        AtBt = outer_product(A.T, B.T)
        self.assertTrue(np.array_equal(AB.T, AtBt))

    def test_example_4_1_4(self):
        probs = probabilities([3-4j, 7+2j])
        self.assertAlmostEqual(25./78., probs[0], 5)
        self.assertAlmostEqual(53. / 78., probs[1], 5)

    def test_problem_5_1_2(self):
        v = [15 - 3.4j, 2.1 - 16j]
        norm_v = norm(v)
        self.assertAlmostEqual(22.292823957, norm_v, 5)
        vn = normalize(v)
        self.assertAlmostEqual(1.0, norm(vn), 5)

    def test_problem_5_1_4(self):
        q0 = vector([1, 0])
        q1 = vector([0, 1])
        q01 = outer_product(q0, q1)
        self.assertEqual("[0 1 0 0]", str(q01.ravel()))
        q11 = outer_product(q1, q1)
        self.assertEqual("[0 0 0 1]", str(q11.ravel()))
        result = 3*q01+2*q11
        self.assertEqual("[0 3 0 2]", str(result.ravel()))

    def test_problem_5_3_1(self):
        u = CNOT @ CNOT
        self.assertTrue(is_unit_matrix(u))

    def test_problem_5_3_2(self):
        t = tofoli()
        u = t @ t
        self.assertTrue(is_unit_matrix(u))

    def test_problem_5_3_4(self):
        f = fredkin()
        u = f @ f
        self.assertTrue(is_unit_matrix(u))

    def test_problem_5_4_1(self):
        self.assertTrue(is_unit_matrix(PAULI_X @ PAULI_X.H))
        self.assertTrue(is_unit_matrix(PAULI_Y @ PAULI_Y.H))
        self.assertTrue(is_unit_matrix(PAULI_Z.H @ PAULI_Z))

    def test_problem_5_4_3(self):
        self.assertTrue(is_unit_matrix(PAULI_X @ PAULI_X))
        self.assertTrue(is_unit_matrix(PAULI_Y @ PAULI_Y))
