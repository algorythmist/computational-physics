import numpy as np
from numpy import sin, cos, exp
from scipy.linalg import kron


# OPERATIONS


def inner(v1, v2):
    return np.vdot(v1, v2)


def vector(list):
    return np.array([list]).T


def outer_product(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    return kron(m1, m2)


def norm(v):
    v = np.array(v)
    return np.real(np.sqrt(inner(v, v)))


def distance(v1, v2):
    return norm(v1 - v2)


def normalize(v):
    v = np.array(v)
    return v / norm(v)


def bits_to_vector(bit_string):
    number = bits_to_int(bit_string)
    v = np.zeros((2 << len(bit_string) - 1)).astype(int)
    v[number] = 1
    return v


def bits_to_int(bit_string):
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

# GATES
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

PAULI_X = np.matrix([[0, 1], [1, 0]])
PAULI_Y = np.matrix([[0, -1j], [1j, 0]])
PAULI_Z = np.matrix([[1, 0], [0, -1]])

HADAMARD = np.matrix([[1, 1], [1, -1]]) / np.sqrt(2)


def identity(dimension):
    return np.diag(np.ones(dimension))


def tofoli():
    tof = np.diag(np.ones(8))
    tof[6, 6] = 0.
    tof[6, 7] = 1.
    tof[7, 6] = 1.
    tof[7, 7] = 0.
    return tof


def fredkin():
    fred = np.diag(np.ones(8))
    fred[5, 5] = 0.
    fred[5, 6] = 1.
    fred[6, 5] = 1.
    fred[6, 6] = 0.
    return fred


def rotation_around_x(theta):
    return np.matrix([[cos(theta / 2), -1j * sin(theta / 2)],
                      [-1j * sin(theta / 2), cos(theta / 2)]])


def rotation_around_y(theta):
    return np.matrix([[cos(theta / 2), -sin(theta / 2)],
                      [sin(theta / 2), cos(theta / 2)]])


def rotation_around_z(theta):
    return np.matrix([[exp(-1j * theta / 2), 0],
                      [0, exp(1j * theta / 2)]])


def rotation_around_axis(axis, theta):
    if len(axis) != 3:
        raise ValueError("Axis must be a 3D vector")
    product = axis[0] * PAULI_X + axis[1] * PAULI_Y + axis[2] * PAULI_Z
    return identity(2) * cos(theta / 2) - 1j * sin(theta / 2) * product


def phase_shift(theta):
    return np.matrix([[1, 0]], [0, exp(1j * theta)])


def hadamard():
    return np.array([[1, 1], [1, -1]])/np.sqrt(2)


def is_unit_matrix(u):
    for i, j in np.ndindex(u.shape):
        if i == j and u[i, j] != 1.:
            return False
        if i != j and u[i, j] != 0.:
            return False
    return True

def build_Uf(f):
    Uf = np.zeros(shape=(4,4), dtype=int)
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
