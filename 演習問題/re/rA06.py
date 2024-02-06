n, q = map(int, input().split())
a = list(map(int, input().split()))

L = [0] * q
R = [0] * q

for s in range(q):
    L[s], R[s] = map(int, input().split())

ans = [0] * (n + 1)
ans[0] = 0

for s in range(n):
    ans[s + 1] = ans[s] + a[s]

for t in range(q):
    print(ans[R[t]] - ans[L[t] - 1])
