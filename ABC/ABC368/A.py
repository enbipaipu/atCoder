N , K = map(int, input().split())

A = list(map(int, input().split()))

for s in range((N-K), N):
    print(A[s], end=" ")


for s in range(N-K):
    print(A[s], end=" ")
    
