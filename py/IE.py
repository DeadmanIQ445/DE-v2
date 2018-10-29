from py import Printer, Data, Functions


class IE(Data.Data):
    def __init__(self, x0=0, y0=1,xs=0, xf=10, n=50):
        super().__init__(x0, y0, xs, xf, n)
        self.improved_e()

    def improved_e(self):
        for i in range(1, len(self.x)):
            k1 = Functions.f(self.x[i - 1], self.y[i - 1])
            k2 = Functions.f(self.x[i], self.y[i - 1] + self.h * k1)
            self.y[i] = self.y[i - 1] + (self.h / 2) * (k1 + k2)


ie = IE()
Printer.show_graph([ie.x], [ie.y], ["IE"], "Improved Euler's Method")
