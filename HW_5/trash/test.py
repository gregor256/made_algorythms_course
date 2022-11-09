import sys
from HW_5_a import MAX_RAND, P, HashTable

n = 20


def solve(verbose=True, method='std_in'):
    res = []
    table = HashTable()
    if method == 'std_in':
        content = sys.stdin
    else:
        content = method.split('\n')
    for line in content:
        print(line)
        if verbose:
            # print(table.__dict__)
            print(table.array)
            print(table.corpses)
            # print(table.multiplier)
        if line == '\n':
            break
        task = line.split()
        if task:
            command, x = task[0], int(task[1])
            if verbose:
                print(command, x)
            if command == 'insert':
                table.put(x)
            elif command == 'exists':
                if table.get(x):
                    if verbose:
                        print(x, 'true')
                    else:
                        res.append('true')
                else:
                    if verbose:
                        print(x, 'false')
                    else:
                        res.append('false')
            else:
                table.delete(x)

    return res


ans = solve(False, method="""insert 0
insert 1
insert 2
insert 3
insert 4
insert 5
insert 6
insert 7
insert 8
insert 9
insert 10
insert 11
insert 12
insert 13
insert 14
insert 15
insert 16
insert 17
insert 18
insert 19
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 0
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 1
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 2
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 3
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 4
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 5
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 6
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 7
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 8
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 9
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 10
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 11
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 12
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 13
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 14
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 15
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 16
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 17
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 18
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19
delete 19
exists 0
exists 1
exists 2
exists 3
exists 4
exists 5
exists 6
exists 7
exists 8
exists 9
exists 10
exists 11
exists 12
exists 13
exists 14
exists 15
exists 16
exists 17
exists 18
exists 19


""")

real_res = ['true' for i in range(n)]
for k in range(n):
    real_res += ['false' if m <= k else 'true' for m in range(n)]

assert ans == real_res
print('OK')
# for i, el in enumerate(real_res):
#     print(el, end=' ')
#     if i > 1 and (i + 1) % n == 0:
#         print()
# print()
#
#
# for i, el in enumerate(ans):
#     print(el, end=' ')
#     if i > 1 and (i + 1) % n == 0:
#         print()

