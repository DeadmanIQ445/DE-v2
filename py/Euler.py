from py import Printer, Data, Functions


class Euler(Data.Data):
    def __init__(self, x0=0, y0=2, xs=-2, xf=10, n=50):
        super().__init__(x0, y0, xs, xf, n)
        self.euler()

    def euler(self):
        for j in range(1, len(self.x)):
            self.y[j] = self.h * Functions.f(self.x[j - 1], self.y[j - 1]) + self.y[j - 1]


eu = Euler()
print(eu.x)
print(eu.y)
Printer.show_graph([eu.x], [eu.y], ["Euler"])
