N = int(input())

A = list(map(int, input().split()))
cnt = 0
for s in range(2 * N - 2):
    if A[s] == A[s + 2]:
        cnt += 1

print(cnt)
