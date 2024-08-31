N, M = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)

if s <= M:
    print("infinite")
    exit()

ok = 0
ng = 1000000000

while (abs(ok-ng)>1):
    mid = (ok + ng) // 2
    tmp = 0
    for v in A:
        tmp += min(mid, v)
    if (tmp <= M):
        ok = mid
    else:
        ng = mid

print(ok)
