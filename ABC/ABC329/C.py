N = input()
S = input()


after = "1"
result = set()
count = 1

for x in S:
    if x == after:
        count += 1
    elif x != after:
        count = 1
        after = x
    result.add(x * count)


print(len(result))
