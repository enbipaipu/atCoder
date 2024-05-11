N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
diff = K
for s in A:

    if diff >= s:
        diff -= s

    elif diff < s:
        count += 1
        diff = K - s

count += 1

print(count)
