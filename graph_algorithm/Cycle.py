class Cycle:
    def __init__(self, graph):
        self._marked = []
        self._graph = graph
        self._has_cycle = False
        for v in range(graph.v):
            self._marked.append(0)
        for v in range(self._graph.v):
            if not self._marked[v]:
                self.dfs(v, v)

    def dfs(self, v, u):
        self._marked[v] = 1
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self.dfs(w, v)
            elif w != u:
                self._has_cycle= True
    def has_cycle(self):
        """
        Is it an acyclic graph?

        :rtype: bool
        """
        return self._has_cycle
