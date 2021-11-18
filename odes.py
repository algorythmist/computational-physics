import sympy
import numpy as np
import matplotlib.pyplot as plt


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
