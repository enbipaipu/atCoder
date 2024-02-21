N, S = map(int, input().split())

A = list(map(int, input().split()))

dp = [[None] * (S + 1) for _ in range(N + 1)]

dp[0][0] = True
for s in range(1, S + 1):
    dp[0][s] = False

for t in range(1, N + 1):
    for s in range(0, S + 1):
        if s < A[t - 1]:
            dp[t][s] = dp[t - 1][s]

        if s >= A[t - 1]:
            if dp[t - 1][s] is True or dp[t - 1][s - A[t - 1]] is True:
                dp[t][s] = True
            else:
                dp[t][s] = False

if dp[N][S] is True:
    print("Yes")
else:
    print("No")
