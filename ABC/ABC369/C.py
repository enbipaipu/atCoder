
def f(n):
    return n*(n+1)//2

N = int (input())
A = list(map(int, input().split()))

ans = 0
pre = 0
i = 1

while (i < N-1):
    if A[i]-A[i-1] != A[i+1]-A[i]:
        ans += f(i-pre)
        pre = i
    i+=1

ans += f(i-pre)

print(ans+N)
