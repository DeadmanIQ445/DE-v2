# Class that I used for testing
from matplotlib import pyplot as mp


def show_graph(x, y, labels, header="", y0=-10, yf=10):
    for i in range(len(x)):
        mp.plot(x[i], y[i], label=labels[i])
    mp.ylim(y0, yf)
    mp.xlabel("X")
    mp.ylabel("Y")
    mp.legend()
    mp.title(header)
    mp.grid(True)
    mp.show()


def show_graph_data(data, header="", y0=-10, yf=10):
    mp.plot(data.x,data.y)
    mp.ylim(y0, yf)
    mp.xlabel("X")
    mp.ylabel("Y")
    mp.title(header)
    mp.grid(True)
    mp.show()
