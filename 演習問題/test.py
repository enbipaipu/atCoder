dic = {1: "a", 2: "b", 3: None}
lis = [4, 5, 6, 7, 3]
value = "abcdef"
dic1 = {s: t for s, t in enumerate(value)}
bol = True if value == "abcdea" else False
se = set(["a", "a", "b"])
A = [[None] * 3 for _ in range(4)]
B = [0, 2, 3]
lis2 = [[4, 2, 3], [1, 2, 3], [1, 2, 3]]
lis2.sort()
dic2 = {"1": ["c", "d"], "2": ["a", "b"]}
lis3 = sorted([x for x in dic2.values()])
print(lis3)
