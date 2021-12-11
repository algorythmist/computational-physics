import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as sla


def solve_laplace_1d(constant, u0, u1, N=20):
    """
    Solve the 1D Laplace equation u_xx = constant in the interval [0,1]
    given boundary conditions u(0) and u(1)
    :return:
    """
    dx = 1.0 / (N + 1)
    dx2 = dx ** 2
    A = (np.eye(N, k=-1) - 2 * np.eye(N) + np.eye(N, k=1)) / dx2
    b = constant * np.ones(N)
    b[0] -= u0 / dx2
    b[N - 1] -= u1 / dx2
    return np.hstack([[u0], la.solve(A, b), [u1]])


def solve_laplace_2d_square(ut, ub, ul, ur, N = 100):
    dx = 1.0/(N+1)
    dx2 = dx ** 2
    A_1d = (sp.eye(N, k=-1) - 4 * sp.eye(N) + sp.eye(N, k=1)) / dx2
    A = sp.kron(sp.eye(N), A_1d) + (sp.eye(N**2, k=-N) + sp.eye(N**2, k=N))/dx2
    b = np.zeros((N, N))
    b[0,: ] += ub
    b[-1, :] += ut
    b[:, 0] += ul
    b[:, -1] += ur
    b = - b.reshape(N**2) /dx2
    u = sla.spsolve(A, b)
    u = u.reshape(N, N)
    return np.vstack([
        np.ones((1, N+2))*ub,
        np.hstack([
            np.ones((N, 1))*ul,
            u,
            np.ones((N, 1))*ur
        ]),
        np.ones((1, N+2))*ut
    ])
