S = input()
T = input()

N = len(S)
M = len(T)

dp = [[0] * (M + 1) for _ in range(N + 1)]
# https://qiita.com/Gamari0009/items/adf21c20ea16cc991fb8
for i in range(0, N + 1):
    for s in range(0, M + 1):
        if i >= 1 and s >= 1 and S[i - 1] == T[s - 1]:
            dp[i][s] = max(dp[i - 1][s], dp[i][s - 1], dp[i - 1][s - 1] + 1)
        elif i >= 1 and s >= 1:
            dp[i][s] = max(dp[i - 1][s], dp[i][s - 1])
        elif i >= 1:
            dp[i][s] = dp[i - 1][s]
        elif s >= 1:
            dp[i][s] = dp[i][s - 1]

print(dp[N][M])
