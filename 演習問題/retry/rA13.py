N, K = map(int, input().split())

A = list(map(int, input().split()))

S = [0] * N + 1

for i in range(1, N + 1):
    S[i] = S[i - 1]
    while 