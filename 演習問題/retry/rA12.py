def check(second, N, K, arr):
    sum = 0
    for i in range(N):
        sum += second // arr[i]
    if sum >= K:
        return True
    return False


N, K = map(int, input().split())

A = list(map(int, input().split()))


L = 0
R = N - 1

while L < R:
    mid = (L + R) // 2
    ans = check(mid, N, K, A)

    if ans:
        R = mid
    if not ans:
        L = mid + 1

print(L)
