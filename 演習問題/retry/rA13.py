N, K = map(int, input().split())

A = list(map(int, input().split()))

S = [0 for _ in range(N)]

L, R = 0, 1

while R < N:
    if L == R:
        R += 1
    dif = A[R] - A[L]
    if dif <= K:
        S[L] += 1
        if R + 1 <= N:
            R += 1
        elif R + 1 > N:
            L += 1
    elif dif > K:
        L += 1

print(S)
