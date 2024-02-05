s = input()

result = ""
for m in s:
    if m == ".":
        result = ""
        continue
    result += m
print(result)
