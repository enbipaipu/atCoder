n = int(input())
result = 0

a = list(map(int, input().split()))

for s in range(n):
    result += a[s]
    if result < 0:
        result = 0


print(result)
