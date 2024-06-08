N, M = map(int, input().split())

H = list(map(int, input().split()))

result = 0
for s in range(N):
    M -= H[s]
    if M == 0:
        result = s + 1
        break
    elif M < 0:
        result = s
        break

if M > 0:
    print(N)
else:
    print(result)
