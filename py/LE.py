import operator


class LE:
    def __init__(self, ivp, method):
        self.x = ivp.x.copy()
        self.y = list(map(operator.sub, ivp.y, method.y))
