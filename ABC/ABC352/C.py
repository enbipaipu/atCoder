N = int(input())
all_kata = 0
max_atama = 0

for _ in range(N):
    A, B = map(int, input().split())
    all_kata += A
    diff = B - A
    if diff > max_atama:
        max_atama = diff

print(max_atama + all_kata)
