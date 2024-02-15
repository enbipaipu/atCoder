import sys

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def binary(arr, num):
    L = 0
    R = len(arr)
    while L < R:
        mid = (L + R) // 2
        if arr[mid] > num:
            R = mid
        if arr[mid] < num:
            L = mid + 1
        if arr[mid] == num:
            return True
    return False


P = []
Q = []

for s in range(N):
    for t in range(N):
        P.append(A[s] + B[t])
        Q.append(C[s] + D[t])

Q.sort()

for i in range(len(P)):
    boo = binary(Q, K - P[i])
    if boo is True:
        print("Yes")
        sys.exit(0)
print("No")
