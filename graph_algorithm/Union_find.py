class UnionFind:
    def __init__(self, n):
        self._count = n
        self._id = range(n)

    @property
    def count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pass

    def find(self, q):
        pass
