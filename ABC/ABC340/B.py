Q = int(input())


L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[i], R[i] = map(int, input().split())

ans = []

for i in range(Q):
    if L[i] == 1:
        ans.append(R[i])
    if L[i] == 2:

        print(ans[-R[i]])
