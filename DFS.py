class Search:
    def __init__(self, graph, s):
        self._graph = graph
        self._s = s
        self._marked = []
        self._count = 0
        for i in range(self._graph.v()):
            self._marked.append(0)

    def depth_first_search(self):
        return self.dfs(self._s)

    def dfs(self, s):
        self._marked[s] = 0
        self._count = self._count+1
        for adj in self._graph.adj(s):
            if not self._marked[adj]:
                self.dfs(adj)

    def count(self):
        return self.count()

    def marked(self, v):
        return self._marked[v]
