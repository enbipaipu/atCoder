S = input()
dic = {s: t for t, s in enumerate(S)}
SS = [s for s in S]
a = [t for t in SS if t != SS[-1]]
ans = None
if len(a) > 1:
    ans = SS[-1]
else:
    ans = a[0]

print(dic[ans] + 1)
