import numpy as np
from numpy import sin, cos, exp
from scipy.linalg import kron

from qc.gates import hadamard, identity


# OPERATIONS


def vector(list):
    """
    Convert an array or list to a column vector
    :param list: the array or list
    :return: a column vector
    """
    return np.array([list]).T


def inner_product(v1, v2):
    return np.vdot(v1, v2)


def outer_product(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return kron(m1, m2)


def norm(v):
    v = np.array(v)
    return np.real(np.sqrt(inner_product(v, v)))


def distance(v1, v2):
    return norm(v1 - v2)


def normalize(v):
    v = np.array(v)
    return v / norm(v)


def bits_to_vector(bit_string: str):
    """
    Convert a bit string of length n to a vector of length 2^n
    :param bit_string:
    :return:
    """
    number = bits_to_int(bit_string)
    v = np.zeros((2 << len(bit_string) - 1)).astype(int)
    v[number] = 1
    return v


def bits_to_int(bit_string: str) -> int:
    """
    Convert a bit string to the an integer
    :param bit_string:
    :return:
    """
    n = len(bit_string) - 1
    number = 0
    for b in bit_string:
        number += (int(b) << n)
        n -= 1
    return number


def state_from_bloch(theta, phi):
    """
    Given the bloch angles, construct the corresponding mixed state
    :param theta: Angle with z-axis
    :param phi: Angle on x-y plane
    :return: a 2D complex vector
    """
    return cos(theta) * np.array([1, 0]) + exp(phi * 1j) * sin(theta) * np.array([0, 1])


def probabilities(state):
    """
    Given a mixed state vector, return an array of probabilities,
    such that p_i is the probability that a measurement will produce the state i
    :param state:
    :return:
    """
    return [np.real(np.vdot(x, x)) for x in normalize(state)]


def is_unit_matrix(u):
    for i, j in np.ndindex(u.shape):
        if i == j and u[i, j] != 1.:
            return False
        if i != j and u[i, j] != 0.:
            return False
    return True


def build_Uf(f):
    Uf = np.zeros(shape=(4, 4), dtype=int)
    if f(0) == 0:
        Uf[0, 0] = 1
        Uf[1, 1] = 1
    else:
        Uf[0, 1] = 1
        Uf[1, 0] = 1
    if f(1) == 0:
        Uf[2, 2] = 1
        Uf[3, 3] = 1
    else:
        Uf[2, 3] = 1
        Uf[3, 2] = 1
    return Uf


def deutsch(f):
    phi_0 = bits_to_vector("01")
    H = hadamard()
    U1 = outer_product(H, H)
    phi_1 = U1 @ phi_0
    print(f'phi_1 = {phi_1}')
    Uf = build_Uf(f)
    phi_2 = Uf @ phi_1
    print(f'phi_2 = {phi_2}')
    U2 = outer_product(H, identity(2))
    phi_3 = U2 @ phi_2
    print(f'phi_3 = {phi_3}')
    if phi_3[0] == 0 and phi_3[1] == 0:
        return 'BALANCED'
    if phi_3[2] == 0 and phi_3[3] == 0:
        return 'CONSTANT'
    raise ValueError("Algorithm failed!")
