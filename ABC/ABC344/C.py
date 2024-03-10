from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

AB_sum = sorted(set(a + b for a in A for b in B))

for x in X:
    found = False
    for c in C:
        if x - c < 0:
            continue
        idx = bisect_left(AB_sum, x - c)
        if idx < len(AB_sum) and AB_sum[idx] == x - c:
            found = True
            break
    print("Yes" if found else "No")
