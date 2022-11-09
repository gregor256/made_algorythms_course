class Node:
    def __init__(self, content):
        self.content = content
        self.minimum = None
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        if self.head:
            new_node.link = self.head
            if value > self.head.minimum:
                new_node.minimum = self.head.minimum
        if new_node.minimum is None:
            new_node.minimum = value
        self.head = new_node
        self.size += 1

    def print_elements(self):
        cur = self.head
        while cur is not None:
            print(cur.content, cur.minimum)
            cur = cur.link

    def erase_last(self):
        if self.size > 0:
            result = self.head.content
            self.head = self.head.link
            return result


class Stack:
    def __init__(self):
        self.container = LinkedList()

    def push(self, x):
        self.container.insert(x)

    def pop(self):
        return self.container.erase_last()

    def show_minimum(self):
        print(self.container.head.minimum)


stack = Stack()
tasks = int(input())
for _ in range(tasks):
    command = tuple(map(int, input().split()))
    if command[0] == 1:
        stack.push(command[1])
    elif command[0] == 2:
        stack.pop()
    else:
        stack.show_minimum()
