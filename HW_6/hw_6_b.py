n, m = map(int, input().split())
dp1 = []
for i in range(n):
    dp1.append(list(map(int, input().split())))

dp = [[0 for _ in range(m + 1)]]


for row in dp1:
    dp.append([0] + row)

# for row in dp:
#     print(row)
#
# print()
#
# print()

parents = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] += dp[i - 1][j]
            parents[i][j] = [i - 1, j]

        else:
            dp[i][j] += dp[i][j - 1]
            parents[i][j] = [i, j - 1]

# for row in dp:
#     print(row)

# print()
#
# for row in parents:
#     print(row)
# print()
order = []
i, j = n, m
while not (i == 0 and j == 0):
    i, j = parents[i][j]
    order.append((i, j))
order = order[::-1]
order.append([n, m])
# print(order)
order_str = ''
i = 3
while i < len(order):
    if order[i][0] == order[i - 1][0]:
        order_str += 'R'
    else:
        order_str += 'D'
    i += 1
print(dp[n][m])
print(order_str)
