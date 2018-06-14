from collections import deque


class BreadFirstSearch:
    def __init__(self, graph, s):
        self._s = s
        self._marked = []
        self._path_to = []
        self._graph = graph

        for i in range(graph.v):
            self._marked.append(0)
            self._path_to.append(-1)

    def bread_first_search(self):
        return self.bfs(self._s)

    def bfs(self, v):
        v_deque = deque([])
        self._marked[v] = 1
        v_deque.append(v)

        while len(v_deque):
            v = v_deque.popleft()
            for w in range(self._graph.abj(v)):
                if not self.marked(w):
                    v_deque.append(w)
                    self._marked[v] = 1
                    self._path_to[w] = v

    def marked(self, v):
        return self._marked[v]

    def has_path_to(self, v):
        return self.marked(v)

    def path_to(self, v):
        ret = []

        if self.marked(v):
            while v != self._s:
                ret.append(self._path_to[v])
                v = self._path_to[v]
        return ret
