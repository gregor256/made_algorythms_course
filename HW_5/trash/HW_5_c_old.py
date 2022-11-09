import random
import sys
from collections import deque

DEFAULT_SIZE = 1_000_000
MAX_RAND = int(1e4)
P = int(1e9 + 7)


class Node:
    def __init__(self, pair):
        self.pair = pair
        self.link = None
        self.link_back = None


class LinkedList:
    def __init__(self, verbose=False):
        self.head = None
        self.tail = None
        self.size = 0
        self.verbose = verbose

    def insert(self, pair):
        new_node = Node(pair)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.link_back = self.tail
            # self.tail.link_back exists
            # new_node.link default None
            self.tail.link = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, key):
        if self.head is None:
            return
        if key == self.head.pair[0]:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.link
                self.head.link_back = None
            self.size -= 1
        else:
            prev = self.head
            cur = prev.link
            while cur is not None and cur.pair[0] != key:
                prev = cur
                cur = prev.link
            if cur:
                prev.link = cur.link
                if cur.link is not None:
                    cur.link.link_back = prev
                if cur == self.tail:
                    self.tail = prev
                self.size -= 1

    def print_elements(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(f'{cur.pair=}')
            if cur.link_back:
                print(f'{cur.link_back.pair=}')
            else:
                print('cur.link_back.pair', None)
            if cur.link:
                print(f'{cur.link.pair=}')
            else:
                print('cur.link.pair', None)
            cur = cur.link

    # def change_value(self, key, value):
    #     if self.head is None:
    #         return
    #     cur = self.head
    #     while cur is not None:
    #         if cur.pair[0] == key:
    #             cur.pair[1] = value
    #             break
    #         cur = cur.link

    def get(self, key):
        cur = self.head
        while cur is not None:
            if cur.pair[0] == key:
                return cur
            cur = cur.link
        return None


class HashTable:
    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.multiplier = random.randint(1, MAX_RAND)
        self.array = [LinkedList() for _ in range(self.size)]
        self.order = LinkedList()

    @staticmethod
    def char_num(char):
        return ord(char) - ord('a') + 1

    def my_hash(self, string):
        result = 1
        for letter in string:
            result = ((result * self.multiplier) % P) % self.size
            result = ((result + self.char_num(letter)) % P) % self.size
        return result

    def put(self, key, value):
        pos = self.my_hash(key)
        node = self.array[pos].get(key)
        if node is not None:
            node.pair[1] = value
            # self.order.change_value(key, value)
        else:
            self.array[pos].insert([key, value])
            self.order.insert([key, value])

    def delete(self, key):
        pos = self.my_hash(key)
        self.array[pos].delete(key)
        self.order.delete(key)

    def get(self, key):
        pos = self.my_hash(key)
        return self.array[pos].get(key)

    def get_neighbour(self, key, further=True):
        current = self.order.get(key)
        if current is not None:
            if further:
                neighbour_node = current.link
            else:
                neighbour_node = current.link_back
            if neighbour_node is not None:
                neighbour_key = neighbour_node.pair[0]
                neighbour_value = self.get(neighbour_key)
                if neighbour_value is not None:
                    return neighbour_value
        else:
            return None


def solve():
    hash_table = HashTable()
    for line in sys.stdin:
        if line == '\n':
            break
        task = line.split()
        if task:
            command, *args = task
            if command in ('put', 'p'):
                hash_table.put(args[0], args[1])

            elif command in ('get', 'g'):
                got = hash_table.get(args[0])
                if got is not None:
                    print(got.pair[1])
                else:
                    print('none')

            elif command in ('prev', 'pr'):
                got = hash_table.get_neighbour(args[0], further=False)
                if got is not None:
                    print(got.pair[1])
                else:
                    print('none')

            elif command in ('next', 'n'):
                got = hash_table.get_neighbour(args[0], further=True)
                if got is not None:
                    print(got.pair[1])
                else:
                    print('none')

            elif command in ('delete', 'd'):
                hash_table.delete(args[0])
            else:
                break


solve()
