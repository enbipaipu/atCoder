N, Q = map(int, input().split())

T = list(map(int, input().split()))

to = [True] * (N)

for s in range(Q):
    if to[T[s] - 1]:
        to[T[s] - 1] = False
    else:
        to[T[s] - 1] = True

ans = 0

for s in to:
    if s is True:
        ans += 1

print(ans)
