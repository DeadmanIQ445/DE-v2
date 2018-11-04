import numpy as np
from py import Functions


class Data:
    def __init__(self, x0=1, y0=3, xs=1, xf=18.2, n=100):
        self.x0 = x0
        self.xs = xs
        self.xf = xf
        self.n = n
        self.c = Functions.in_value(x0, y0)
        self.x = np.linspace(self.xs, self.xf, num=n)
        self.y = [0] * len(self.x)
        self.y[0] = Functions.real_f(self.x[0], self.c)

    def copy(self, data):
        self.x0 = data.x0
        self.xs = data.xs
        self.xf = data.xf
        self.n = data.n
        self.c = data.c
        self.x = data.x.copy()
        self.y = data.y.copy()
