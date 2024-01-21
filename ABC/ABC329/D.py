n, m = map(int, input().split())
value = list(map(int, input().split()))
result = [0] * n

for s in range(m):
    x = value[s] - 1
    result[x] = result[x] + 1
    winner = result.index(max(result)) + 1
    print(winner)
