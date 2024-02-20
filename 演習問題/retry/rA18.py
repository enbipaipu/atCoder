N, S = map(int, input().split())

A = list(map(int, input().split()))

dp = [[None] * (S + 1) for _ in range(N + 1)]

dp[0][0] = True
for t in range(1, S + 1):
    dp[0][t] = False

for n in range(1, N + 1):
    for s in range(0, S + 1):
        if s < A[n - 1]:
            dp[n][s] = dp[n - 1][s]

        if s >= A[n - 1]:
            if dp[n - 1][s] is True or dp[n - 1][s - A[n - 1]] is True:
                dp[n][s] = True
            else:
                dp[n][s] = False

if dp[N][S] is True:
    print("Yes")
else:
    print("No")
