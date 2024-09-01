N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)

a = 0
b = 0
i = 0

while i < N:
    a += A[i]
    b += B[i]
    if a > X or b > Y:
        break
    i+=1

print(i if i == N else i+1)


