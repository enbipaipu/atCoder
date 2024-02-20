# N, W = map(int, input().split())

# weight = [None] * (N + 1)
# value = [None] * (N + 1)
# for n in range(1, N + 1):
#     weight[n], value[n] = map(int, input().split())

N, W = 4, 7
weight = [None, 3, 3, 5, 1]
value = [None, 13, 17, 29, 10]

dp = [[-1] * (W + 1) for _ in range(N + 1)]


dp[0][0] = 0
for s in range(1, N + 1):
    for t in range(0, W + 1):
        if t < weight[s]:
            dp[s][t] = dp[s - 1][t]
        if t >= weight[s]:
            dp[s][t] = max(dp[s - 1][t], dp[s - 1][t - weight[s]] + value[s])

for s in dp:
    print(s)

print(max(dp[N]))
