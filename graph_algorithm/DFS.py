class DepthFirstSearch:
    def __init__(self, graph, s):
        self._graph = graph
        self._s = s
        self._marked = []
        self._count = 0
        self._path_to = []
        for i in range(self._graph.v):
            self._marked.append(0)
            self._path_to.append(-1)
        self.dfs(self._s)

    def dfs(self, s):
        self._marked[s] = 1
        self._count = self._count+1
        for w in self._graph.adj(s):
            if not self._marked[w]:
                self._path_to[w] = s
                self.dfs(w)

    def count(self):
        return self._count

    def marked(self, v):
        return self._marked[v]

    def has_path_to(self, v):
        return self.marked(v)

    def path_to(self, v):
        """
        A path from s to v
        :rtype: list
        """
        ret = []

        if self.marked(v):
            while v != self._s:
                ret.append(self._path_to[v])
                v = self._path_to[v]
        return ret

