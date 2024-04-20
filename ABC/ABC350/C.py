N = int(input())
A = list(map(int, input().split()))

result = []
for i in range(N):
    while A[i] != i + 1:
        correct_pos = A[i] - 1
        A[i], A[correct_pos] = A[correct_pos], A[i]  # 要素を正しい位置に移動
        result.append((i + 1, correct_pos + 1))  # 1-indexedに基づいて記録

print(len(result))
for swap in result:
    print(swap[0], swap[1])
