def binary(arr, num):
    L = 0
    R = len(arr)
    while L < R:
        mid = (L + R) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            R = mid
        if arr[mid] < num:
            L = mid + 1


N = int(input())

A = list(map(int, input().split()))

sorted_A = list(sorted(set(A)))

B = [None] * N
for s in range(N):
    B[s] = binary(sorted_A, A[s]) + 1
Answer = [str(i) for i in B]
for s in Answer:
    print("".join(s))
