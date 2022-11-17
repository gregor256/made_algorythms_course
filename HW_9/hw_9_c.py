from sys import setrecursionlimit
import threading


class Graph:
    def __init__(self, neighbours):
        self.vert_num = len(neighbours)
        self.neighbours = neighbours
        self.cyclic = False

    def dfs_for_sorting(self, _v, _used, _ans):
        _used[_v] = True
        for neighbour in self.neighbours[_v]:
            if not _used[neighbour]:
                self.dfs_for_sorting(neighbour, _used, _ans)
        _ans.append(_v)

    def dfs_cycle_find(self, _v, _color):
        if self.cyclic:
            return
        _color[_v] = 1
        for neighbour in self.neighbours[_v]:
            if _color[neighbour] == 0:
                self.dfs_cycle_find(neighbour, _color)
            if _color[neighbour] == 1:
                self.cyclic = True
        _color[_v] = 2

    def is_graph_cyclic(self):
        color = [0 for _ in range(self.vert_num)]
        for v in range(self.vert_num):
            if color[v] == 0:
                self.dfs_cycle_find(v, color)

    def get_topo_sorting(self):
        self.is_graph_cyclic()
        if self.cyclic:
            return -1
        used = [False for _ in range(self.vert_num)]
        ans = []
        for v in range(self.vert_num):
            if not used[v]:
                self.dfs_for_sorting(v, used, ans)

        return ans[::-1]


def read_graph():
    n_vertices, n_edges = map(int, input().split())
    graph = [[] for _ in range(n_vertices)]
    for edge in range(n_edges):
        vertex_1, vertex_2 = map(int, input().split())
        graph[vertex_1 - 1].append(vertex_2 - 1)
    return graph


def print_array(_array):
    if isinstance(_array, list):
        for i, element in enumerate(_array):
            if i < len(_array):
                print(element + 1, end=' ')
            else:
                print(element + 1)
    else:
        print(-1)


def main():
    graph = Graph(read_graph())
    print_array(graph.get_topo_sorting())


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
