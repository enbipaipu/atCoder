H, W = map(int, input().split())

X = [None] * H
for i in range(H):
    X[i] = list(map(int, input().split()))

Q = int(input())

A = [None] * Q
B = [None] * Q
C = [None] * Q
D = [None] * Q

for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int, input().split())

dif = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

for s in range(1, H + 1):
    for t in range(1, W + 1):
        dif[s][t] = dif[s][t - 1] + X[s - 1][t - 1]

for s in range(1, H + 1):
    for t in range(1, W + 1):
        dif[s][t] = dif[s - 1][t] + dif[s][t]

for s in range(Q):
    print(
        dif[C[s]][D[s]]
        + dif[A[s] - 1][B[s] - 1]
        - dif[C[s]][B[s] - 1]
        - dif[A[s] - 1][D[s]]
    )
