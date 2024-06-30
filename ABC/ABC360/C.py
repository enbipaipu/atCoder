N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

dic = {s: set() for s in range(1, N + 1)}
result = 0

for i, s in enumerate(A, start=1):
    dic[s].add(W[i - 1])


for s in range(1, N + 1):
    while len(dic[s]) > 1:
        x = min(dic[s])
        dic[s].remove(x)
        result += x

print(result)
