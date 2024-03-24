N, S = map(int, input().split())

a = list(map(int, input().split()))

dp = [[None] * (S + 1) for s in range(N + 1)]

dp[0][0] = True

for s in range(1, S + 1):
    dp[0][s] = False

for i in range(1, N + 1):
    for t in range(0, S + 1):
        if t < a[i - 1]:
            dp[i][t] = dp[i - 1][t]

        if t >= a[i - 1]:
            if dp[i - 1][t] is True or dp[i - 1][t - a[i - 1]] is True:
                dp[i][t] = True
            else:
                dp[i][t] = False

print("Yes" if dp[N][S] is True else "No")
