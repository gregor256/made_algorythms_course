from sys import setrecursionlimit
import threading


def dfs(_graph, _v, _colors, _current_color):
    _colors[_v] = _current_color
    for neighbour in _graph[_v]:
        if _colors[neighbour] == 0:
            dfs(_graph, neighbour, _colors, _current_color)


def print_array(_array):
    for i, element in enumerate(_array):
        if i < len(_array) - 1:
            print(element, end=' ')
        else:
            print(element)


def main():
    # graph = [[3 - 1],
    #          [4 - 1],
    #          [],
    #          []]
    vert_num, edges_num = map(int, input().split())
    graph = [[] for _ in range(vert_num)]
    for edge in range(edges_num):
        vertex_1, vertex_2 = map(int, input().split())
        graph[vertex_1 - 1].append(vertex_2 - 1)
        graph[vertex_2 - 1].append(vertex_1 - 1)

    colors = [0 for _ in range(vert_num)]
    current_color = 0
    for v in range(vert_num):
        if colors[v] == 0:
            current_color += 1
            dfs(graph, v, colors, current_color)
    print(current_color)
    print_array(colors)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
