N, K = map(int, input().split())

A = list(map(int, input().split()))

for s in A:
    if s % K == 0:
        print(s // K)
