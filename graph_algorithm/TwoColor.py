class TwoColor:
    def __init__(self, graph):
        self._marked = []
        self._graph = graph
        self._color = []
        self._is_two_color = True
        for v in range(graph.v):
            self._marked.append(0)
            self._color.append(False)
        for v in range(graph.v):
            if not self._marked[v]:
                self.dfs(v)

    def dfs(self, v):
        self._marked[v] = 1
        for w in range(self._graph.v):
            if not self._marked:
                self._color[w] = not self._color[v]
                self.dfs(w)
            elif self._color[w] == self._color[v]:
                self._is_two_color = False

    def is_two_color(self):
        """
        Is it a Dichroic graph?

        :rtype: bool
        """
        return self._is_two_color
