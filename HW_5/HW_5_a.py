import random
import sys

MAX_RAND = int(1e4)
P = int(1e9 + 7)


class HashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.corpses_amount = 0
        self.alive_amount = 0
        self.multiplier = random.randint(1, MAX_RAND)
        self.array = [None for _ in range(self.capacity)]
        self.corpses = [False for _ in range(self.capacity)]

    def my_hash(self, key):
        if key is not None:
            return ((self.multiplier * key) % P) % self.capacity

    def further(self, pos):
        return (pos + 1) % self.capacity

    def put(self, key):
        if self.alive_amount + self.corpses_amount > self.capacity / 2:
            self.rehashing()
        pos = self.my_hash(key)
        while self.array[pos] is not None:
            if self.array[pos] == key:
                if self.corpses[pos]:
                    self.corpses[pos] = False
                    self.alive_amount += 1
                    self.corpses_amount -= 1
                    return
                else:
                    return
            pos = self.further(pos)
        self.array[pos] = key
        self.alive_amount += 1

    def get(self, key):
        pos = self.my_hash(key)
        while self.array[pos] is not None:
            if self.array[pos] == key:
                if not self.corpses[pos]:
                    return True
                else:
                    return False
            pos = self.further(pos)
        return False

    def delete(self, key):
        pos = self.my_hash(key)
        while self.array[pos] is not None:
            if self.array[pos] == key:
                self.corpses[pos] = True
                self.corpses_amount += 1
                self.alive_amount -= 1
                break
            pos = self.further(pos)

    def rehashing(self):
        old_array = self.array.copy()
        old_capacity = self.capacity
        self.capacity = self.capacity * 2
        self.array = [None for _ in range(self.capacity)]
        self.alive_amount = 0
        self.corpses_amount = 0
        self.multiplier = random.randint(1, MAX_RAND)
        for i in range(old_capacity):
            if old_array[i] is not None and not self.corpses[i]:
                self.put(old_array[i])
        self.corpses = [False for _ in range(self.capacity)]


def solve():
    table = HashTable()
    for line in sys.stdin:
        if line == '\n':
            break
        task = line.split()
        if task:
            command, x = task[0], int(task[1])
            if command in ('insert', 'i'):
                table.put(x)
            elif command in ('exists', 'e'):
                if table.get(x):
                    print('true')
                else:
                    print('false')
            elif command in ('delete', 'd'):
                table.delete(x)
            else:
                break


solve()
