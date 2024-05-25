N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)
A = sorted(A)

for s in range(N + M - 1):
    for t in range(N - 1):
        co_tru = C[s] == A[t]
        ne_tru = C[s + 1] == A[t + 1]

        if co_tru and ne_tru:
            print("Yes")
            exit()

print("No")
