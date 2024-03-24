n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None] * (n + 1)

dp[1] = 0
dp[2] = A[0]
for s in range(3, n + 1):
    dp[s] = min(dp[s - 1] + A[s - 2], dp[s - 2] + B[s - 3])

ans = [n]
place = n

while True:
    if place == 1:
        break
    elif dp[place] - A[place - 2] == dp[place - 1]:
        ans.append(place - 1)
        place -= 1
    else:
        ans.append(place - 2)
        place -= 2
ans = [str(s) for s in reversed(ans)]

print(len(ans))
print(" ".join(ans))
