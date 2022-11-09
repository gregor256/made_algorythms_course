class CyclicSpreadingArray:  # Суслик))))
    def __init__(self):
        self.array = [0, 0]
        self.capacity = 2
        self.head = 0
        self.tail = 0

    def further(self, pos):
        return (pos + 1) % self.capacity

    def size(self):
        return (self.capacity - self.head + self.tail) % self.capacity

    def change_size(self, spreading):

        if spreading:
            new_capacity = self.capacity * 2
        else:
            new_capacity = self.capacity // 2
        new_array = [0 for _ in range(new_capacity)]
        old_array_pos = self.head
        new_array_pos = 0
        while new_array_pos < self.size():
            new_array[new_array_pos] = self.array[old_array_pos]
            new_array_pos += 1
            old_array_pos = self.further(old_array_pos)
        self.capacity = new_capacity
        self.array = new_array
        self.head = 0
        self.tail = new_array_pos

    def insert(self, x):
        if self.size() + 2 > self.capacity:
            self.change_size(spreading=True)
        self.array[self.tail] = x
        self.tail = self.further(self.tail)

    def get_head(self):
        return self.array[self.head]

    def chop_head(self):
        self.head = self.further(self.head)
        if 0 < self.size() < self.capacity / 4:
            self.change_size(spreading=False)


class Queue:
    def __init__(self):
        self.container = CyclicSpreadingArray()

    def pop(self):
        res = self.container.get_head()
        self.container.chop_head()
        return res

    def push(self, x):
        self.container.insert(x)


tasks_num = int(input())
queue = Queue()
for i in range(tasks_num):
    task = input()
    if task == '-':
        print(queue.pop())
    else:
        mock, value = task.split()
        queue.push(int(value))

