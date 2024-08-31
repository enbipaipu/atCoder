N = int(input())

ans = 0
right = 0
left = 0

for _ in range(N):
    A, S = input().split()
    A = int(A)

    if S == "L":
        if left != 0:
            ans += abs(left-A)
        left = A
    else:
        if right != 0:
            ans += abs(right-A)
        right = A
print(ans)