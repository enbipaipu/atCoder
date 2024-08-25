N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))

A.append(9000000000000)

res = 0
r = 0

for l in range(0, n):
    while A[r] < A[l]+M:
        r+=1
    res = max(res, r-1)
print(res)