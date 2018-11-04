from py import Data, Functions


class Euler(Data.Data):
    def __init__(self, x0=0, y0=2, xs=-2, xf=10, n=50, data=None):
        if data is None:
            super().__init__(x0, y0, xs, xf, n)
            self.euler()
        else:
            self.copy(data)
            self.euler()

    def euler(self):
        h = self.x[-2] - self.x[-3]
        for j in range(1, len(self.x)):
            self.y[j] = h * Functions.f(self.x[j - 1], self.y[j - 1]) + self.y[j - 1]
