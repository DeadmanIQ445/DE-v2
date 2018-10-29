import numpy as np


def f(x, y):
    return -y - x


def real_f(x, c):
    return 1 - x + c/np.exp(x)


def in_value(x, y):
    return (y + x - 1) * np.exp(x)
