from py import Data, Functions


class IVP(Data.Data):
    def __init__(self, x0=0, y0=2, xs=-2, xf=4, n=50, data=None):
        if data is None:
            super().__init__(x0, y0, xs, xf, n)
            self.ivp()
        else:
            self.copy(data)
            self.ivp()

    def ivp(self):
        for j in range(1, len(self.x)):
            self.y[j] = Functions.real_f(self.x[j], self.c)
