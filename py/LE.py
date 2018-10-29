from py import IVP, Printer, Functions,Euler, IE, RK
import operator


class LocalErr(IVP.SolvedIVP):
    def __init__(self, method, x0=0, y0=2, xs=-2, xf=4, n=50 ):
        super().__init__(x0, y0, xs, xf, n)
        self.le(method)

    def le(self, method):
        self.y = list(map(operator.sub, self.y, method.y))


le_eu = LocalErr(Euler.Euler(x0=0, y0=2, xs=-2, xf=4, n=50 ))
le_ie = LocalErr(IE.IE(x0=0, y0=2, xs=-2, xf=4, n=50 ))
le_rk = LocalErr(RK.RK(x0=0, y0=2, xs=-2, xf=4, n=50 ))
Printer.show_graph([le_eu.x, le_ie.x, le_rk.x], [le_eu.y, le_ie.y, le_rk.y], ["Euler", "IE", "RK"], "LE", -0.01, 0.2)
