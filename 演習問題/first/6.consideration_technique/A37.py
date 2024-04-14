N, M, B = map(int, input().split())

A = list(map(int, input().split()))

C = list(map(int, input().split()))


A = [x * M for x in A]
C = [x * N for x in C]

ans = N * M * B + sum(A) + sum(C)

print(ans)
