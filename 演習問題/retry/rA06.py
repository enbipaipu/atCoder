N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [None] * (Q)
R = [None] * (Q)

for s in range(Q):
    L[s], R[s] = map(int, input().split())

S = [None] * (N + 1)
S[0] = 0

for s in range(N):
    S[s + 1] = A[s] + S[s]

for s in range(Q):
    print(S[R[s]] - S[L[s] - 1])
