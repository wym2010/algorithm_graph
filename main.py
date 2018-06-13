import re
from Union_find import UnionFind
if __name__ == '__main__':
    with open('c:\\Users\\wangym20804\\Desktop\\tinyUF.txt') as f:

        n = int(f.readline())
        uf = UnionFind(n)

        for line in f:
            pq = map(int, re.split(r' *', line))
            if uf.connected(pq[0],pq[1]):
                continue
            uf.union(pq[0], pq[1])
            print(pq[0], ' ', pq[1])

        print(uf.count, 'components')


