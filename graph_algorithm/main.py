import re
# from Union_find import UnionFind
from Cycle import Cycle
from BFS import BreadFirstSearch
from DFS import DepthFirstSearch
from Graph import Graph
from CC import CC
from TwoColor import TwoColor
if __name__ == '__main__':
    with open('c:\\Users\\wangym20804\\Desktop\\tinyUF.txt') as f:

        n = int(f.readline())
        graph = Graph(n)
        for line in f:
            vw = map(int, re.split(r' *', line))
            graph.add_edge(vw[0], vw[1])
        print(graph)
    bfs = BreadFirstSearch(graph, 0)
    dfs = DepthFirstSearch(graph, 0)
    cc = CC(graph)
    cycle = Cycle(graph)
    two_color = TwoColor(graph)

    print(bfs.path_to(4))
    print(dfs.path_to(4))
    print(cc.count())
    print(cycle.has_cycle())
    print(two_color.is_two_color())