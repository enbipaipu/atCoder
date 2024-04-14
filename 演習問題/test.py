# dic = {1: "a", 2: "b", 3: None}
# lis = [4, 5, 6, 7, 3]
# value = "abcdef"
# dic1 = {s: t for s, t in enumerate(value)}
# bol = True if value == "abcdea" else False
# se = set(["a", "a", "b"])
# A = [[None] * 3 for _ in range(4)]
# B = [0, 2, 3]
# print(sum(B))

import time

start = time.time()
original_list = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in original_list]
print(doubled_list)
finish = time.time()
print(finish - start)

start2 = time.time()
original_list = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda x: x * 2, original_list))
print(doubled_list)
finish2 = time.time()
print(finish2 - start2)

start3 = time.time()
original_list = [1, 2, 3, 4, 5]
doubled_list = []
for x in original_list:
    doubled_list.append(x * 2)
print(doubled_list)
finish3 = time.time()
print(finish3 - start3)
