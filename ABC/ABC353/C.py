N = int(input())
ll = 10**8

A = [int(s) % ll for s in input().split()]

result = 0
for s in range(N - 1):
    for t in range(s + 1, N):
        result += (A[s] + A[t]) % ll


print(result)
