D, N = map(int, input().split())

ans = [24] * (D)

for s in range(N):
    L, R, H = map(int, input().split())
    for t in range(L - 1, R):
        ans[t] = min(ans[t], H)

result = 0
for s in range(D):
    result += ans[s]
print(result)
