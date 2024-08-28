N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

all_sum = sum(W)
box = [{0} for _ in range(N)]

for s in range(N):
    box[A[s]-1].add(W[s])

sums = 0

for s in box:
    sums += max(s)

print(all_sum-sums)