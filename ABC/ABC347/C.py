N, A, B = map(int, input().split())

D = list(map(int, input().split()))
ans = []
for s in D:
    x = s % (A + B)
    if x == 0 or x > A:
        ans.append(False)
    else:
        ans.append(True)

print("Yes" if all(ans) else "No")
