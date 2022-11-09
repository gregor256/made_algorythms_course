class SpreadingArray:
    def __init__(self):
        self.array = [0, 0]
        self.size = 0
        self.capacity = 2

    def change_size(self, spreading):
        if spreading:
            self.capacity = self.capacity * 2
        else:
            self.capacity //= 2
        new_array = [0 for _ in range(self.capacity)]
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def erase_last(self):
        self.size -= 1
        if 0 < self.size < self.capacity / 4:
            self.change_size(spreading=False)

    def insert(self, x):
        if self.size == self.capacity:
            self.change_size(spreading=True)
        self.array[self.size] = x
        self.size += 1

    def get(self, num):
        if 0 <= num <= self.size:
            return self.array[num]


class Stack:
    def __init__(self):
        self.container = SpreadingArray()

    def pop(self):
        res = self.container.get(self.container.size - 1)
        self.container.erase_last()
        return res

    def push(self, x):
        self.container.insert(x)


def solve(string):
    stack = Stack()
    array = string.split()
    for el in array:
        if el == '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)

        elif el == '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)

        elif el == '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)

        else:
            stack.push(int(el))
    return stack.container.array[0]


print(solve(input()))
