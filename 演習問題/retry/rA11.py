N, X = map(int, input().split())

A = list(map(int, input().split()))

L = 0
R = N - 1

while L < R:
    mid = (L + R) // 2
    if X <= A[mid]:
        R = mid
    elif X > A[mid]:
        L = mid + 1
    # +++++
    elif X == A[mid]:
        L = mid
        break
    # +++++
print(L + 1)
