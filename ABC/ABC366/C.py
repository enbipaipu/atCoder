q = int(input())
cnt = [0] * 1000000
ans = 0

for _ in range(q):
    t,*x = map(int,input().split())
    if t == 1:
        x[0] -= 1
        cnt[x[0]] += 1
        if cnt[x[0]] == 1:
            ans += 1
    elif t == 2:
        x[0] -= 1
        cnt[x[0]] -= 1
        if cnt[x[0]] == 0:
            ans -= 1
    else:
        print(ans)
