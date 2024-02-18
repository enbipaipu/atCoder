N, M, K = map(int, input().split())

large = max(N, M)
small = min(N, M)
results = []
number = 1
while len(results) < K:
    value1 = small * number
    value2 = large * number
    if not value1 % large == 0:
        results.append(value1)
    if not value2 % small == 0:
        results.append(value2)
    number += 1
print(max(results))
