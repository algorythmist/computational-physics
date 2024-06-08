import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
def fractional_derivative(p, a):
    coeff = 1
    result = 0
    for n in range(1, p.degree()):
        f = p.deriv(n - 1)
        # Update the term for the current n
        coeff *= (a - (n - 1)) / n
        # Add the term to the result
        result += coeff * f
    return result


def plot_polynomial(p, points=100):
    x = np.linspace(p.domain[0], p.domain[1], points)
    return plt.plot(x, p(x))


p = Polynomial.fromroots([-1.5,0,1], domain =[-2,2])
print(p.degree())
f = fractional_derivative(p, 0.5)
plot_polynomial(f)
plt.show()