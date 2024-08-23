dic = {1: "a", 2: "b", 3: "c"}
lis = [4, 5, 6, 7, 3, 3, 4]
value = "abcdef"
dic1 = {s: t for s, t in enumerate(value)}
bol = True if value == "abcdea" else False
se = set(["a", "a", "b"])
A = [[None] * 3 for _ in range(4)]

ll = 10**8
t = set()
a = 1
b = 2
if b > a:
    t.add((a, b))
else:
    t.add((b, a))
print(t)