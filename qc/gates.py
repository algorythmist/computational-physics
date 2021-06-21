import numpy as np
from numpy import exp, sin, cos


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

NOT = PAULI_X

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


def hadamard(power: int = 1):
    if power == 1:
        return np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    n = 2 ** power
    h = np.ones(shape=(n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            bit_string1 = int_to_bits(i, power)
            bit_string2 = int_to_bits(j, power)
            if bit_inner_product(bit_string1, bit_string2) == 1:
                h[i][j] = -1
    return h / np.sqrt(n)


def int_to_bits(n: int, size: int) -> str:
    return "{:0b}".format(n).zfill(size)


def bit_inner_product(bit_string1: str, bit_string2: str):
    """
    The inner product of two bit strings defined as (s1[0]and s2[0]) xor (s1[1]and s2[1]) xor ...
    :param bit_string1:
    :param bit_string2:
    :return:
    """
    if len(bit_string1) != len(bit_string2):
        raise ValueError("Bit strings must be the same length")
    result = int(bit_string1[0]) and int(bit_string2[0])
    for i in range(1, len(bit_string2)):
        result ^= (int(bit_string1[i]) and int(bit_string2[i]))
    return result
