#入力
N = int(input())
A = list(map(int,input().split())) 

B = []

#解法
for i in range(N):
    B.append(A[i])

    while len(B) != 1 and B[-1] == B[-2]:
        B[-2] = B[-2] + 1
        B.pop()

#出力
print(len(B))