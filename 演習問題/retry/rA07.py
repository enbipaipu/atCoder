D = int(input())

N = int(input())

L = [None] * N
R = [None] * N

for i in range(N):
    L[i], R[i] = map(int, input().split())

B = [0] * (D + 2)

for i in range(N):
    B[L[i]] += 1
    B[R[i] + 1] -= 1

S = [None] * (D + 2)
S[0] = 0

for i in range(D):
    S[i + 1] = S[i] + B[i + 1]

for i in range(1, D + 1):
    print(S[i])
