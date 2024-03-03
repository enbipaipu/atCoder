A, B = map(int, input().split())
ans = 0
purasu = A + B
for s in range(0, 10):
    ans = s
    if s != purasu:
        break

print(ans)
