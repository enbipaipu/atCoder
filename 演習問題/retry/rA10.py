N = int(input())

A = list(map(int, input().split()))

D = int(input())

L = [None] * D
R = [None] * D

for i in range(D):
    L[i], R[i] = map(int, input().split())


P = [0] * (N + 2)
Q = [0] * (N + 2)


for i in range(1, N + 1):
    P[i] = max(A[i - 1], P[i - 1])

for i in reversed(range(1, N + 1)):
    Q[i] = max(A[i - 1], Q[i + 1])


for i in range(D):
    print(max(P[L[i]-1], Q[R[i]+1]))