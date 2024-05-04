n, x, y, z = map(int, input().split())
ans = False
t = 1


if x >= y:
    t = -1

for s in range(x, y + t, t):
    if s == z:
        ans = True

print("Yes" if ans else "No")
