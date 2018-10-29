from py import Printer, Data, Functions


class RK(Data.Data):
    def __init__(self, x0=0, y0=1, xs=0, xf=10, n=50):
        super().__init__(x0, y0, xs, xf, n)
        self.runge_kutta()

    def runge_kutta(self):
        for i in range(1, len(self.x)):
            k1 = Functions.f(self.x[i - 1], self.y[i - 1])
            k2 = Functions.f(self.x[i - 1] + self.h / 2, self.y[i - 1] + self.h * k1 / 2)
            k3 = Functions.f(self.x[i - 1] + self.h / 2, self.y[i - 1] + self.h * k2 / 2)
            k4 = Functions.f(self.x[i], self.y[i - 1] + self.h * k3)
            self.y[i] = self.y[i - 1] + (self.h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


rk = RK()
Printer.show_graph([rk.x], [rk.y], ["Runge-Kutta"])
