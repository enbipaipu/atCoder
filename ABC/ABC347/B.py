S = input()

ans = set()

for t in S:
    ans.add(t)

for t in range(0, len(S) + 1):
    for i in range(t + 1, len(S) + 1):
        if t == i:
            continue
        ans.add(S[t:i])

print(len(ans))
