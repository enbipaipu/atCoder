S = input()
T = input()

N = len(S)
M = len(T)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        if S[n - 1] == T[m - 1]:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1], dp[n - 1][m - 1] + 1)
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])
