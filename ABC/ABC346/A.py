n = int(input())
a = list(map(int, input().split()))

b = [None] * (n - 1)

for s in range(1, n):
    b[s - 1] = a[s] * a[s - 1]

t = [str(x) for x in b]

for s in t:
    print("".join(s))
