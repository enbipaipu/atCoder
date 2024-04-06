N = int(input())

corect = dict()

for s in range(N):
    a, c = map(int, input().split())
    if corect.get(c) is not None and corect.get(c) < a:
        continue
    corect[c] = a

lis = [x for x in corect.values()]

print(max(lis))
