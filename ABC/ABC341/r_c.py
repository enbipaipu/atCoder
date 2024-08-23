import copy

H, W, N = map(int, input().split())
T = input()
S = []

for i in range(H):
    S.append(input())

count = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == "#":
            continue
        I = copy.copy(i)
        J = copy.copy(j)
        ok = True
        for t in T:
            if t == "L":
                J -= 1
            elif t == "R":
                J += 1
            elif t == "U":
                I -= 1
            elif t == "D":
                I += 1

            if S[I][J] == "#":
                ok = False
                break
        if ok is True:
            count += 1

print(count)
