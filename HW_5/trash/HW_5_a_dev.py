import random
import sys

MAX_RAND = int(1e4)
P = int(1e9 + 7)


with open('out.txt', 'w') as f:
    class HashTable:
        def __init__(self, capacity=2048):
            self.capacity = capacity
            self.corpses_amount = 0
            self.alive_amount = 0
            self.multiplier = random.randint(1, MAX_RAND)
            # self.multiplier = 1000
            self.array = [None for _ in range(self.capacity)]
            self.corpses = [False for _ in range(self.capacity)]

        def my_hash(self, key):
            if key is not None:
                # return ((self.multiplier * key) % P) % self.capacity
                return key % self.capacity
                # return 0

        def further(self, pos):
            return (pos + 1) % self.capacity

        def put(self, key):
            if self.alive_amount + self.corpses_amount > self.capacity / 2:
                self.rehashing(spreading=True)
            pos = self.my_hash(key)
            # print(self.array)
            # print(pos)
            while not self.array[pos] is None:
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
            step = 0
            while not self.array[pos] is None and \
                    step < 2 * self.capacity:
                if self.array[pos] == key:
                    if not self.corpses[pos]:
                        return True
                    else:
                        return False
                pos = self.further(pos)
                step += 1
            return False

        def delete(self, key):
            # print('delete', key)
            pos = self.my_hash(key)
            step = 0
            while self.array[pos] is not None and step < 2 * self.capacity:
                if self.array[pos] == key:
                    # print(f'{pos=}')
                    self.corpses[pos] = True
                    self.corpses_amount += 1
                    self.alive_amount -= 1
                    break
                pos = self.further(pos)
                step += 1
            # print(f'{self.alive_amount=}', f'{self.capacity / 4=}')
            # print('after deleting', self.corpses)
            if 4 < self.alive_amount < self.capacity / 8 and self.capacity > 8:
                self.rehashing(spreading=False)

        def rehashing(self, spreading):
            # print('rehashing', f'{spreading=}')
            # print('>>>', self.array, self.corpses)
            old_array = self.array.copy()
            old_capacity = self.capacity
            if spreading:
                self.capacity = self.capacity * 2
            else:
                print('zip', file=f)
                self.capacity = self.capacity // 2
            self.array = [None for _ in range(self.capacity)]
            self.alive_amount = 0
            self.corpses_amount = 0
            self.multiplier = random.randint(1, MAX_RAND)
            for i in range(old_capacity):
                if not old_array[i] is None and not self.corpses[i]:
                    self.put(old_array[i])
                    # print(f'{old_array=}', file=f)
                    to_print = [x for x in self.array if x is not None]
                    # noinspection PyTypeChecker
                    print('new_array', sorted([x for x in self.array if x is not None]), file=f)
            self.corpses = [False for _ in range(self.capacity)]


    def solve(verbose=True, method='std_in'):
        table = HashTable()
        if method == 'std_in':
            content = sys.stdin
        else:
            content = method.split('\n')
        for line in content:
            if line == '\n':
                break
            task = line.split()
            if task:
                command, x = task[0], int(task[1])
                if verbose:
                    print(command, x, file=f)
                if command in ('insert', 'i'):
                    table.put(x)
                elif command in ('exists', 'e'):
                    if table.get(x):
                        if verbose:
                            print(x, 'true', file=f)
                        else:
                            print('true', file=f)
                    else:
                        if verbose:
                            print(x, 'false', file=f)
                        else:
                            print('false', file=f)
                elif command in ('delete', 'd'):
                    table.delete(x)

                elif command == 'exit':
                    break
                else:
                    continue
                if verbose:
                    print(f'{table.capacity=}', file=f)
                    print(f'{table.alive_amount=}', file=f)
                    print(f'{table.corpses_amount=}', file=f)
                    # print(f'{table.corpses=}', file=f)
                    # print(f'{table.corpses_amount=}')
                    # print(table.array)
                    # print(table.corpses)


    solve(True, method='std_in')
