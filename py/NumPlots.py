from py import Data, Euler, RK, IE, LE, IVP


class Plots:
    def __init__(self, x0, xs, xf, y0, n):
        self.x0 = x0
        self.xs = xs
        self.xf = xf
        self.y0 = y0
        self.n = n

        self.data = Data.Data(x0=x0, xs=xs, xf=xf, y0=y0, n=n)
        self.euler = Euler.Euler(data=self.data)
        self.ie = IE.IE(data=self.data)
        self.rk = RK.RK(data=self.data)
        self.ivp = IVP.IVP(data=self.data)
        self.le_eu = LE.LE(self.ivp, self.euler)
        self.le_ie = LE.LE(self.ivp, self.ie)
        self.le_rk = LE.LE(self.ivp, self.rk)
