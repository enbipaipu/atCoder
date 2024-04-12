n, r = map(int, input().split())
M = 1000000007
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

b = 1
for i in range(1, r + 1):
    b = (b * i) % M

for i in range(1, n - r + 1):
    b = (b * i) % M
