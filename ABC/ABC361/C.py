N, K = map(int, input().split())

A = list(map(int, input().split()))

results = set()

A_sort = sorted(A)


for s in range(K + 1):
    results.add((A_sort[-(K + 1 - s)] - A_sort[s]))

print(min(results))
