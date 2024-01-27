s = input()

dic = {}

for l in s:
    if l in dic.keys():
        dic[l] += 1
    else:
        dic[l] = 1

max_value = max(dic.values())

max_keys = [key for key, value in dic.items() if value == max_value]
result = sorted(max_keys)

print(result[0])
