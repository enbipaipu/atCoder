n = int(input())

ans = ""

for s in range(1, n + 1):
    if s % 3 == 0:
        ans += "x"
    else:
        ans += "o"
print(ans)
