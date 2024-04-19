N, L = map(int, input().split())

A = [None] * (N)
B = [None] * (N)

for s in range(N):
    A[s], B[s] = input().split()
    A[s] = int(A[s])


ans = 0


for i in range(N):
    if B[i] == "E":
        ans = max(ans, L - A[s])
    if B[i] == "W":
        ans = max(ans, A[s])

print(ans)
