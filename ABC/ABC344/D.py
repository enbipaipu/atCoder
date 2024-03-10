T = input()
N = int(input())
A = [input().split()[1:] for _ in range(N)]

INF = float("inf")
dp = [[INF] * (len(T) + 1) for _ in range(len(A) + 1)]
dp[0][0] = 0

for i in range(1, len(A) + 1):
    for j in range(len(T) + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        for s in A[i - 1]:
            k = len(s)
            if j + k <= len(T) and T[j : j + k] == s:
                dp[i][j + k] = min(dp[i][j + k], dp[i - 1][j] + 1)

ans = dp[len(A)][len(T)]
if ans == INF:
    ans = -1
print(ans)
