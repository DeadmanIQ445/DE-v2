import numpy as np


def f(x, y):
    return -x + y*(2*x+1)/x


def real_f(x, c):
    return 0.5*x + x*c*np.exp(2*x)


def in_value(x, y):
    return (2*y-x)/(2*x*np.exp(2*x))
