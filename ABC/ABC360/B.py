S, T = input().split()

le = len(S)
se = set()

for t in range(2, le - 1):
    for L in range(t):
        result = ""
        for i in range(L, le, t):
            result += S[i]
        se.add(result)


print(se)
print("Yes" if (T in se) else "No")
