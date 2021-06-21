import random

import matplotlib.pyplot as plt


def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    if b == 1:
        return 1
    r = a % b
    return gcd(b, r)


def find_coprime(n: int) -> int:
    while True:
        b = random.randint(1, n - 1)
        if gcd(n, b) == 1:
            return b


def powers(a: int, n: int, r: int = None):
    if r is None:
        r = n-1
    return [(a ** k) % n for k in range(1, r)]


def find_period(a: int, n: int):
    return next(k for k in range(1, n-1) if (a**k) % n == 1)


if __name__ == '__main__':
    n = 371
    a = 24
    r = 526
    p = powers(a, n, r)
    plt.bar(range(1, r), p)
    plt.show()
