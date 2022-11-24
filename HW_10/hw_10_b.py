from queue import PriorityQueue

MAX_W = 1e10


def dijkstra(_graph):
    _nodes_num = len(_graph)
    used = [False for _ in range(_nodes_num)]
    dists = [0 if _ == 0 else MAX_W for _ in range(_nodes_num)]
    q = PriorityQueue()
    q.put((0, 0))
    used_num = 0
    while used_num < _nodes_num:
        if q.empty():
            break
        next_node = q.get()[1]
        if not used[next_node]:
            used[next_node] = True
            used_num += 1
            for u, w in _graph[next_node]:
                if not used[u]:
                    dists[u] = min(dists[u], dists[next_node] + w)
                    q.put((dists[u], u))
    return dists


def read_graph():
    _nodes_num, _edges_num = map(int, input().split())
    _graph = [[] for _ in range(_nodes_num)]
    for edge in range(_edges_num):
        start, end, weight = tuple(map(int, input().split()))
        _graph[start - 1].append((end - 1, weight))
        _graph[end - 1].append((start - 1, weight))
    return _graph


def pretty_print(array):
    for i, element in enumerate(array):
        if i < len(array) - 1:
            print(element, end=' ')
        else:
            print(element)


if __name__ == '__main__':
    graph = read_graph()
    pretty_print(dijkstra(graph))
