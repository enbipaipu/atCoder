A, B = map(int, input().split())

if A == B:
    print(1)
    exit()

big = A
small = B
if A < B:
    big = B
    small = A

mid = (big-small)/2
if mid*10 != int(mid)*10:
    print(2)
else:
    print(3)