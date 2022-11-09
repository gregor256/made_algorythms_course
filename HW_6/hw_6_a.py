INF = int(1e9)
n, k = map(int, input().split())
dp = [0] + list(map(int, input().split())) + [0]
parents = [-1]

for i in range(1, n):
    M = -INF
    chosen_i = -1
    for j in range(1, k + 1):
        if i - j >= 0:
            if dp[i - j] > M:
                M = dp[i - j]
                chosen_i = i - j
    parents.append(chosen_i)
    dp[i] = M + dp[i]

order = []
i = n - 1
while i > 0:
    i = parents[i]
    order.append(i + 1)
order = order[::-1]
order.append(n)
print(dp[n - 1])
print(len(order) - 1)
print(" ".join(str(x) for x in order))
