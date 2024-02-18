N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    S, T = map(int, input().split())
    x = A[i] // S
    A[i] -= S * x
    A[i + 1] += T * x


print(A[N - 1])
