N = int(input())
A = list(map(int, input().split()))

D = int(input())
L = [None] * D
R = [None] * D

for s in range(D):
    L[s], R[s] = map(int, input().split())


for s in range(D):
    print(max(A[: L[s] - 1] + A[R[s] - 1 : len(A)]))
