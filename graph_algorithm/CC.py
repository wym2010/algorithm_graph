
class CC:
    def __init__(self, graph):
        self._marked = []
        self._id = []
        self._graph = graph
        self._count = 0

        for v in range(graph.v):
            self._marked.append(0)
            self._id.append(0)

        for v in range(graph.v):
            if not self._marked[v]:
                self.dfs(v)
                self._count = self._count+1

    def dfs(self, v):
        self._marked[v] = 1
        self._id[v] = self._count
        for w in self._graph.adj(v):
            if not self._marked[w]:
                self.dfs(w)



    def connected(self, v, w):
        """
        v w connected?
        :rtype: bool
        """
        return self._id[v] == self._id[w]

    def count(self):
        """
        Connected component number

        :rtype: int
        """
        return self._count

    def id(self, v):
        """
        Connected component identifier


        :rtype: int
        """
        return self._id[v]


