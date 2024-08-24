N = int(input())
A = list(map(int, input().split()))
count = 0
A = sorted(A, reverse=True)
for _ in range(6000):
    A[0]-=1
    A[1]-=1
    count+=1
    A = sorted(A, reverse=True)
    if A[1] == 0:
        break

print(count)
    