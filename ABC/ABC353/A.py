N = int(input())

H = list(map(int, input().split()))

hi = H[0]
num = 1
for s in range(1, N):
    if H[s] > hi:
        hi = H[s]
        num = s + 1
        break


if num == 1:
    print(-1)
else:
    print(num)
