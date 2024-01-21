S = input()
a = S.count("A")
b = S.count("B")
c = S.count("C")
if "A" * a + "B" * b + "C" * c == S:
    print("Yes")
    exit()
print("No")

# ソートを使う
S = input()
if "".join(sorted(S)) == S:
    print("Yes")
else:
    print("No")

# 正規表現を使う
from re import fullmatch

if fullmatch("A*B*C*", input()):
    print("Yes")
else:
    print("No")
