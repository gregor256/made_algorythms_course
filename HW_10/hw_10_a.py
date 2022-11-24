from collections import deque

DELTA = (
    (1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)
)


def knight_bfs(_start_x, _start_y, _target_x, _target_y, _used):
    _N = len(used)
    _parents = [[[-1, -1] for _ in range(_N)] for __ in range(_N)]
    _parents[_start_x][_start_y] = [_start_x, _start_y]
    queue = deque()
    _used[_start_x][_start_y] = True
    queue.append((_start_x, _start_y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in DELTA:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= _N - 1 \
                    and 0 <= new_y <= _N - 1 \
                    and not _used[new_x][new_y]:
                _used[new_x][new_y] = True
                queue.append((new_x, new_y))
                _parents[new_x][new_y] = [x, y]
                if new_x == _target_x and new_y == _target_y:
                    return _parents
    return _parents


def restore_path(_start_x, _start_y, _target_x, _target_y, _parents):
    son = [_target_x, _target_y]
    reversed_path_to_node = [son]
    while not(son[0] == _start_x and son[1] == _start_y):
        parent = _parents[son[0]][son[1]]
        if parent == [-1, -1]:
            return
        son = parent
        reversed_path_to_node.append(parent)
    path_to_node = reversed_path_to_node[::-1]
    print(len(path_to_node))
    for step_x, step_y in path_to_node:
        print(step_x + 1, step_y + 1)


if __name__ == '__main__':
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    used = [[False for _ in range(N)] for __ in range(N)]
    parents = knight_bfs(x1 - 1, y1 - 1, x2 - 1, y2 - 1, used)

    restore_path(x1 - 1, y1 - 1, x2 - 1, y2 - 1, parents)
