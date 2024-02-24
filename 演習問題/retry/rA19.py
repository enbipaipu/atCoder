N, W = map(int, input().split())

we = [None] * (N + 1)
va = [None] * (N + 1)

for s in range(1, N + 1):
    we[s], va[s] = map(int, input().split())

dp = [[0] * (W + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for w in range(0, W + 1):
        if w < we[n]:
            dp[n][w] = dp[n - 1][w]
        if we[n] <= w:
            dp[n][w] = max(dp[n - 1][w], dp[n - 1][w - we[n]] + va[n])

print(dp[N][W])
