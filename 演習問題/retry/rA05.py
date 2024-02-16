# 入力
N, K = map(int, input().split())

ans = 0

for s in range(1, N + 1):
    for t in range(1, N + 1):
        whi = K - (s + t)
        if whi >= 1 and whi <= N:
            ans += 1

print(ans)
