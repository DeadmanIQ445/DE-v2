import numpy as np
from py import Functions


class Data:
    def __init__(self, x0=-1, y0=1, xs=0, xf=10, n=50):
        self.x0 = x0
        self.xs = xs
        self.xf = xf
        self.n = n
        self.c = Functions.in_value(x0, y0)
        self.h = (xf - xs) / n
        self.x = np.arange(self.xs, self.xf, self.h)
        self.y = [0]*len(self.x)
        self.y[0] = Functions.real_f(self.x[0], self.c)
