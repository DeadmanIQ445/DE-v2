from py import Data, Printer, Functions


class SolvedIVP(Data.Data):
    def __init__(self, x0=0, y0=2, xs=-2, xf=4, n=50):
        super().__init__(x0, y0, xs, xf, n)
        self.ivp()

    def ivp(self):
        for j in range(1, len(self.x)):
            self.y[j] = Functions.real_f(self.x[j], self.c)


ivp = SolvedIVP()
Printer.show_graph([ivp.x], [ivp.y], "IVP")
