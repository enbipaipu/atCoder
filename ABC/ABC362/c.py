N = int (input())
X = [0 for _ in range(N)]
L = [0 for _ in range(N)]
R = [0 for _ in range(N)]

ans = False

for i in range(N):
    L[i], R[i] = map(int, input().split())

Max = sum(R)

if sum(L) > 0 or Max < 0:
    print("Yes" if ans else "No")
    exit()

current = 0

for i in range(N):
    diff = R[i]-L[i]
    Max -= diff
    
    X[i] = L[i]
    
    if Max <= 0:
        X[i] = L[i] + (-1 * Max)
        ans = True
        current = i+1
        break

for i in range(current, N):
    X[i] = R[i]

print("Yes" if ans else "No")
print(*X)