class Graph:
    def __init__(self, arg):
        if isinstance(arg, int):
            self._V = arg
            self._E = 0
            self._Edge = []

        if isinstance(arg, list):
            self._V = arg[0]
            self._E = arg[1]
            for Edge in arg[2]:
                if set(Edge) not in self._Edge:
                    self._Edge.append(set(Edge))

    @property
    def v(self):
        return self._V

    @property
    def e(self):
        return self._E

    def add_edge(self, v, w):
        if set(v, w) not in self._Edge:
            self._Edge.append(set(v, w))

    def adj(self,v):
        res = []
        for E in self._Edge:
            if v in E:
                res.append((E - set(v))[0])
        return res
