from functools import lru_cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1

def sin(x,n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        s = s + ((y**(2.0*i+1))/factorial(2*i+1))*sign
    return s
x=int(input("x in degrees: "))
n=int(input("number of terms "+"'n'" ": "))
print(round(sin(x,n),2))

#IMLOSSSSSSINIT