from itertools import accumulate

N, Q = map(int, input().split())

A = [0] + list(map(int, input().split()))

L = [None] * (Q)
R = [None] * (Q)

for s in range(Q):
    L[s], R[s] = map(int, input().split())

S = list(accumulate(A))

for s in range(Q):
    print(S[R[s]] - S[L[s] - 1])
