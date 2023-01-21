import sympy
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def apply_ics(solution, ics, x, known_params):
    """
    Apply initial conditions (ics) to an ODE solution
    :param solution: a sympy ODE solution
    :param ics: a dictionary of initial conditions
    :param x: the independent variable
    :param known_params: known parameters should not be substituted
    :return:
    """
    free_params = solution.free_symbols - set(known_params)
    eqs = [
        (solution.lhs.diff(x, n) - solution.rhs.diff(x, n)).subs(x, 0).subs(ics)
        for n in range(len(ics))
    ]
    solution_params = sympy.solve(eqs,free_params)
    return solution.subs(solution_params)


def plot_direction_field(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
    f_np = sympy.lambdify((x, y_x), f_xy, 'numpy')

    x_vec = np.linspace(x_lim[0], x_lim[1], 20)
    y_vec = np.linspace(y_lim[0], y_lim[1], 20)

    if ax is None:
        _, ax = plt.subplots(figsize=(4, 4))

    dx = x_vec[1] - x_vec[0]
    dy = y_vec[1] - y_vec[0]

    for m, xx in enumerate(x_vec):
        for n, yy in enumerate(y_vec):
            Dy = f_np(xx, yy) * dx
            Dx = 0.8 * dx ** 2 / np.sqrt(dx ** 2 + Dy ** 2)
            Dy = 0.8 * Dy * dy / np.sqrt(dx ** 2 + Dy ** 2)
            ax.plot([xx - Dx / 2, xx + Dx / 2],
                    [yy - Dy / 2, yy + Dy / 2], 'b', lw=0.5)
    ax.axis('tight')

    # ax.set_title(r"$%s$" %
    #              (sympy.latex(sympy.Eq(y(x).diff(x), f_xy))),
    #              fontsize=18)

    return ax


def solve_harmonic(m, k, c=0, x0=5, v0=0, span=[0, 10]):
    """
    Solve the harmonic oscilator in 1D
    :param m: mass
    :param k: spring constant
    :param c: dumping coefficient
    :param x0: initial position
    :param v0: initial velocitys
    :param span:
    :return:
    """
    def harmonic(t, q):
        return [q[1], -k * q[0] / m - c * q[1] / m]

    return solve_ivp(harmonic, span, [x0, v0], dense_output=True)
