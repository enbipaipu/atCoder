s = input()
ans = ""
bo = True
for t in s:
    if t != "|" and bo is True:
        ans += t
    elif t == "|" and bo is True:
        bo = False
    elif t == "|" and bo is False:
        bo = True


print(ans)
