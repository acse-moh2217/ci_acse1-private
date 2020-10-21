from functools import lru_cache

__all__ = ['my_sum', 'factorial', 'mysin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1

def mysin(x, order):
    a = x
    s = a
    for i in range(order):
        a *= -1 * x**2 / ((2 * i) * (2 * i + 1))
        s += a
    return s

#IMLOSSSSSSINIT