import copy

H, W, N = map(int, input().split())
T = input()
grid = []

for _ in range(H):
    grid.append(input())

ans = 0

for t in range(H):
    for s in range(W):
        player = grid[t][s]
        if player == "#":
            continue
        ok = False
        for x in T:
            ok = True
            Q = copy.copy(t)
            P = copy.copy(s)

            if x == "L":
                P -= 1
            elif x == "R":
                P += 1
            elif x == "U":
                Q -= 1
            elif x == "D":
                Q += 1
            if grid[Q][P] == "#":
                ok = False
                break
        if ok is True:
            ans += 1
            print(t, s)

print(ans)
