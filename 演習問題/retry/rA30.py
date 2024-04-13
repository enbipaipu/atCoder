n, r = map(int, input().split())
M = 1000000007
a = 1


def power(a, b, m):
    p = a
    Answer = 1
    for i in range(30):
        wari = 2**i
        if (b // wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer


# 逆元と剰余演算 https://math.nakaken88.com/textbook/cp-modulo-operation-inverse-element

# power(b, m - 2, m)はbの逆元を取得するために必要。


def Division(a, b, m):
    return (a * power(b, m - 2, m)) % m


for i in range(1, n + 1):
    a = (a * i) % M

b = 1
for i in range(1, r + 1):
    b = (b * i) % M

for i in range(1, n - r + 1):
    b = (b * i) % M

print(Division())
