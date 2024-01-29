s = input()

ans = "a"

for x in range(ord("b"), ord("z") + 1):
    c = chr(x)
    if s.count(c) > s.count(ans):
        ans = c

print(ans)
