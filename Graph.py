class Graph:
    def __init__(self, arg):
        if isinstance(arg, int):
            self._V = arg
            self._E = 0
            self._Edge = []
            for i in range(self._V):
                self._Edge[i] = []

        if isinstance(arg, list):
            self._V = arg[0]
            self._E = arg[1]
            for Edge in arg[2]:
                if Edge[1] not in self._Edge[Edge[0]]:
                    self._Edge[Edge[0]].append(Edge[1])
                    self._Edge[Edge[1]].append(Edge[0])
                    self._E = self._E+1

    @property
    def v(self):
        return self._V

    @property
    def e(self):
        return self._E

    def add_edge(self, v, w):
        if w not in self._Edge[v]:
            self._Edge[v].append(w)
            self._Edge[w].append(v)

    def adj(self, v):
        return self._Edge[v]

    def degree(self, v):
        return len(self.adj(v))

    def max_degree(self):
        max_degree = 0
        for v in range(self.v()):
            max_degree = max(self.degree(v), max_degree)
        return max_degree

    def avg_degree(self):
        return 2*self._E / self._V

    def number_of_selfloops(self):
        count = 0
        for v in range(self.v()):
            if v in self.adj(v):
                count = count+1
        return count/2

    @staticmethod
    def my_str(v):
        return str(v) + ','

    def __str__(self):
        res = str(self.v()) + 'vertices,' + str(self.e()) + 'edges\n'
        for v in range(self.v()):
            adj_str = list(map(self.my_str, self.adj(v)))
            res = res.join(adj_str) + '\n'
        return res
