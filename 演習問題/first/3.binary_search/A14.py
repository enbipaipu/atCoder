N = int(input())
A = list(map(int, input().split()))


def binary(arr, target):
    L = 0
    R = len(arr)
    while L < R:
        mid = (L + R) // 2
        if target <= arr[mid]:
            R = mid
        if arr[mid] < target:
            L = mid + 1
    return L


T = list(set(A))
T.sort()
B = [None] * N
for i in range(N):
    B[i] = binary(T, A[i])
    B[i] += 1

# 答えを空白区切りで出力
Answer = [str(i) for i in B]
print(" ".join(Answer))
