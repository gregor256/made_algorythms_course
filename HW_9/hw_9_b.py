from sys import setrecursionlimit
import threading


class DummyDict:
    def __init__(self):
        self.array = []

    def get(self, _desired_name):
        for i, name in enumerate(self.array):
            if name == _desired_name:
                return i
        self.array.append(_desired_name)
        return len(self.array) - 1


def dfs(_graph, _v, _used, n=0):
    max_n = n
    # print('n===', n)
    # print(_v)
    _used[_v] = True
    for neighbour in _graph[_v]:
        if not _used[neighbour]:
            max_n = max(max_n, dfs(_graph, neighbour, _used, n + 1))
    return max_n


def read_graph_from_input():
    dummy_dict = DummyDict()
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        line = input()
        reposter, author = line.split()[0].lower(), line.split()[2].lower()
        author_num = dummy_dict.get(author)
        reposter_num = dummy_dict.get(reposter)
        graph[author_num].append(reposter_num)
    return graph


def main():
    graph = read_graph_from_input()
    # print(graph)
    used = [False for _ in range(len(graph))]
    print(dfs(graph, 0, used) + 1)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
