# 累積和の考え方が必要。

n, q = map(int, input().split())
a = list(map(int, input().split()))
a = {y: x for y, x in enumerate(a)}

Q = {}

for s in range(q):
    l, r = map(int, input().split())
    Q[s] = (l, r)

S = {}
S[0] = 0

for i in range(n):
    S[i + 1] = S[i] + a[i]

for j in range(q):
    print(S[Q[j][1]] - S[Q[j][0] - 1])
