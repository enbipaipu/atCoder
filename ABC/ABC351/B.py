N = int(input())
A = ""
B = ""

for _ in range(N):
    A += input()
for _ in range(N):
    B += input()
i = 0
for i in range(N**2):
    if A[i] != B[i]:
        print(i//N + 1, i % N + 1)
        exit()
    i+=1
