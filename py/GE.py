from py import NumPlots
import numpy as np


class GE:
    def __init__(self, n0, nf, x0=1, xs=1, xf=18.2, y0=3):
        self.ge_eu = []
        self.ge_ie = []
        self.ge_rk = []
        for j in range(n0, nf + 1):
            plots = NumPlots.Plots(x0=x0, xs=xs, xf=xf, y0=y0, n=j)
            self.ge_eu.append(max(plots.le_eu.y))
            self.ge_ie.append(max(plots.le_ie.y))
            self.ge_rk.append(max(plots.le_rk.y))
        self.x = np.arange(n0, nf + 1, 1)
