N = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

ans = [None] * (N + 1)
ans[0] = 0
ans[1] = 0
ans[2] = A[0]

for s in range(3, N + 1):
    ans[s] = min(ans[s - 1] + A[s - 2], ans[s - 2] + B[s - 3])

print(ans[N])
