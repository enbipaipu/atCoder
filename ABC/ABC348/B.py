import numpy as np

N = int(input())

X = [None] * N
Y = [None] * N


for s in range(N):
    X[s], Y[s] = map(int, input().split())


for s in range(N):
    dist = 0
    num = 0
    for t in range(N):
        p = np.array([X[s], Y[s]])
        q = np.array([X[t], Y[t]])
        now_dist = np.linalg.norm(p - q)
        if now_dist > dist:
            dist = now_dist
            num = t + 1
    print(num)
