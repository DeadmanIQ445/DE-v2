from matplotlib import pyplot as mp


def show_graph(x, y, labels, header="", y0=-10, yf=10):
    for i in range(len(x)):
        mp.plot(x[i], y[i], label=labels[i])
    mp.ylim(y0, yf)
    mp.xlabel("Value of x")
    mp.ylabel("Value of y")
    mp.legend()
    mp.title("Approximate Solution with " + header)
    mp.grid(True)
    mp.show()
