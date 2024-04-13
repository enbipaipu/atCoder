import sys

S = input()
T = input()
t = T.lower()
count = 0
ans = ""

for s in S:
    if count >= 3:
        break
    st = t[count]

    if s == st:
        ans += s
        count += 1

if ans == t:
    print("Yes")
    sys.exit()

ans += "x"
if count == 2 and ans == t:
    print("Yes")
else:
    print("No")
