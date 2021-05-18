import numpy as np


def hyperbolic_metric(dim):
    d = np.ones(dim)
    d[-1] = -1
    return np.diag(d)


def normalize_spherical(p):
    p = np.array(p)
    norm = np.sqrt(sum(p ** 2))
    return p / norm


def hyperbolic_inner(p, q):
    return np.inner(p[0:-1], q[0:-1]) - p[-1] * q[-1]


def normalize_hyperbolic(p):
    p = np.array(p)
    norm = hyperbolic_inner(p, p)
    if norm >= 0:
        raise ValueError("Vector cannot be normalized")
    return p / -norm


def distance_spherical(p, q):
    return np.arccos(np.inner(p, q))


def distance_hyperbolic(p, q):
    return np.arccosh(-hyperbolic_inner(p, q))
