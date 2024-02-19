N = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

dp = [None] * (N + 1)

dp[1] = 0
dp[2] = A[0]

for s in range(3, N + 1):
    dp[s] = min(dp[s - 1] + A[s - 2], dp[s - 2] + B[s - 3])


route = [N]
place = N
while True:
    if place == 1:
        break
    if dp[place] - A[place - 2] == dp[place - 1]:
        place -= 1
    elif dp[place] - B[place - 3] == dp[place - 2]:
        place -= 2
    route.append(place)


ans = [str(s) for s in reversed(route)]
print(len(ans))
print(" ".join(ans))
