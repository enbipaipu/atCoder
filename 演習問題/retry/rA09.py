H, W, N = map(int, input().split())

A = [None] * N
B = [None] * N
C = [None] * N
D = [None] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())


z = [[0] * (W + 2) for _ in range(H + 2)]
ans = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    z[A[i]][B[i]] += 1
    z[A[i]][D[i] + 1] -= 1
    z[C[i] + 1][B[i]] -= 1
    z[C[i] + 1][D[i] + 1] += 1


for s in range(1, H + 1):
    for t in range(1, W + 1):
        ans[s][t] = ans[s][t - 1] + z[s][t]

for t in range(1, W + 1):
    for s in range(1, H + 1):
        ans[s][t] = ans[s][t] + ans[s - 1][t]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if j >= 2:
            print(" ", end="")
        print(ans[i][j], end="")
    print("")
