N = int(input())
A = list(map(int, input().split()))

# ニム和
xor_sum = A[0]
for s in range(N + 1):
    xor_sum ^= A[s]

print("First" if xor_sum >= 1 else "Second")
