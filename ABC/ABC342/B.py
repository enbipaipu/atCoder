N = int(input())
P = list(map(int, input().split()))
Q = int(input())

dic = {s: t for t, s in enumerate(P)}
ans = []
for _ in range(Q):
    A, B = map(int, input().split())
    dif = dic[A] - dic[B]
    if dif > 0:
        ans.append(B)
    else:
        ans.append(A)

[print(s) for s in ans]
