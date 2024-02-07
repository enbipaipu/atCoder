d = int(input())
n = int(input())

L = [0] * n
R = [0] * n

for s in range(n):
    L[s], R[s] = map(int, input().split())

B = [0] * (d + 2)

for s in range(n):
    B[L[s]] += 1
    B[R[s] + 1] -= 1

ans = [0] * (d + 2)
ans[0] = 0

for s in range(1, d + 1):
    ans[s] = ans[s - 1] + B[s]

for s in range(1, d + 1):
    print(ans[s])
