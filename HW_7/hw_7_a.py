M = 1e9 + 7
P = 199


class StringHash:
    def __init__(self, string):
        self.string = string
        self.hashes = [0 for _ in range(len(string))]
        self.powers = [1 for _ in range(len(string))]
        if string:
            self.hashes[0] = self.my_ord(string[0])
            for i in range(1, len(string)):
                self.hashes[i] = int(self.hashes[i - 1] * P + self.my_ord(string[i]) % M)
                self.powers[i] = int((self.powers[i - 1] * P) % M)

    @staticmethod
    def my_ord(letter):
        return ord(letter) + 10

    def get_hash(self, left, right):
        if not self.string:
            return 0
        if left == 0:
            return self.hashes[right]
        return int((self.hashes[right] - ((self.hashes[left] *
                                           self.powers[right - left]) % M) + M) % M)

    def are_substrings_equal(self, left_1, right_1, left_2, right_2):
        if right_1 - left_1 != right_2 - left_2:
            return False
        return self.get_hash(left_1 - 1, right_1 - 1) == self.get_hash(left_2 - 1, right_2 - 1)


def solve(std_input=True, s='', poses=None):
    if std_input:
        s = input()
        iterations = int(input())
    else:
        iterations = 1
    hash_string = StringHash(s)
    for iteration in range(iterations):
        if std_input:
            task_left_1, task_right_1, task_left_2, task_right_2 = tuple(map(int, input().split()))
        else:
            task_left_1, task_right_1, task_left_2, task_right_2 = poses
        if hash_string.are_substrings_equal(task_left_1, task_right_1, task_left_2, task_right_2):
            # pass
            print('Yes')
        else:
            # pass
            print('No')


if __name__ == '__main__':
    # ss = 'trololo'
    # for a in range(1, len(ss) + 1):
    #     for b in range(a, len(ss) + 1):
    #         for c in range(1, len(ss) + 1):
    #             for d in range(c, len(ss) + 1):
    #                 print(a, b, c, d, end=' --- ')
    #                 solve(False, ss, (a, b, c, d))
    solve()
