n = int(input())

A = list(map(int, input().split()))

ans = 0

for s in A:
    ans += s
print(-ans)
