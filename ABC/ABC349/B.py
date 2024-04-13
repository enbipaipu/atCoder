S = input()

result = {}

limit = 100

for x in S:
    if x in result:
        result[x] += 1
    elif not (x in result):
        result[x] = 0

result2 = sorted(result.values())
ans = True
for s in range(limit):
    x = result2.count(s)
    if x != 0 and x != 2:
        ans = False
        break


print("Yes" if ans else "No")
