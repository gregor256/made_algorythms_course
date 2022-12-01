import sys


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insert(subtree_root, value):
    if subtree_root is None:
        return Node(value)
    elif value < subtree_root.key:
        subtree_root.left = insert(subtree_root.left, value)
    elif value > subtree_root.key:
        subtree_root.right = insert(subtree_root.right, value)
    return subtree_root


def search(subtree_root, value):
    if subtree_root is None:
        return None
    if value == subtree_root.key:
        return subtree_root
    elif value < subtree_root.key:
        return search(subtree_root.left, value)
    else:
        return search(subtree_root.right, value)


def find_max(subtree):
    if subtree is not None:
        while subtree.right is not None:
            subtree = subtree.right
    return subtree


def delete(subtree_root, value):
    if subtree_root is None:
        return None
    if value < subtree_root.key:
        subtree_root.left = delete(subtree_root.left, value)
    elif value > subtree_root.key:
        subtree_root.right = delete(subtree_root.right, value)
    elif subtree_root.left is None and subtree_root.right is None:
        subtree_root = None
    elif subtree_root.left is None:
        subtree_root = subtree_root.right
    elif subtree_root.right is None:
        subtree_root = subtree_root.left
    else:
        subtree_root.key = find_max(subtree_root.left).key
        subtree_root.left = delete(subtree_root.left, subtree_root.key)

    return subtree_root


def forward(root, value):
    subtree_root = root
    result = None
    while subtree_root is not None:
        if subtree_root.key > value:
            result = subtree_root
            subtree_root = subtree_root.left
        else:
            subtree_root = subtree_root.right
    return result


def previous(root, value):
    subtree_root = root
    result = None
    while subtree_root is not None:
        if subtree_root.key < value:
            result = subtree_root
            subtree_root = subtree_root.right
        else:
            subtree_root = subtree_root.left
    return result


def solve():
    tree = None
    for line in sys.stdin:
        if line == '\n':
            break
        task = line.split()
        if task:
            command, x = task[0], int(task[1])
            if command in ('insert', 'i'):
                tree = insert(tree, x)

            elif command in ('exists', 'e'):
                if search(tree, x):
                    print('true')
                else:
                    print('false')

            elif command in ('delete', 'd'):
                if search(tree, x) is not None:
                    tree = delete(tree, x)

            elif command in ('next',):
                forward_element = forward(tree, x)
                if forward_element is None:
                    print('none')
                else:
                    print(forward_element.key)

            elif command in ('prev',):
                previous_element = previous(tree, x)
                if previous_element is None:
                    print('none')
                else:
                    print(previous_element.key)

            else:
                break


if __name__ == '__main__':
    solve()
