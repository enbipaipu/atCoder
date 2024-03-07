"あまりの割り算について https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6"

n, r = map(int, input().split())
M = 1000000007

# 手順 1：分子を求める
a = 1
for i in range(1, n + 1):
    a = (a * i) % M

# 手順 2：分母を求める
b = 1
for i in range(1, r + 1):
    b = (b * i) % M
for i in range(1, n - r + 1):
    b = (b * i) % M

print(a * pow(b, M - 2, M) % M)
