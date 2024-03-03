N = int(input())
ans = []
for s in range(N):
    A = list(map(int, input().split()))
    T = []
    for t, L in enumerate(A):
        if L == 1:
            T.append(t + 1)
    ans.append(T)

[print(" ".join(str(t) for t in s)) for s in ans]
