n, k = map(int, input().split())

allsum = k * (k + 1) // 2

A = list(map(int, input().split()))
A = list(sorted(set(A)))

A = [s for s in A if s <= k]

asum = sum(A)

ans = allsum - asum


print(ans)
