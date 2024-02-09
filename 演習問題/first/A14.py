N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def binary(arr, target):
    L = 0
    R = len(arr)
    while L < R:
        mid = (L + R) // 2
        if target <= arr[mid]:
            R = mid
        if target > arr[mid]:
            L = mid + 1

    return L


P = []

for x in range(N):
    for y in range(N):
        P.append(A[x] + B[y])

Q = []

for z in range(N):
    for w in range(N):
        Q.append(C[z] + D[w])

Q.sort()

for i in range(len(P)):
    pos1 = binary(Q, K - P[i])
    if pos1 < N * N and Q[pos1] == K - P[i]:
        print("Yes")
        exit(0)
print("No")
