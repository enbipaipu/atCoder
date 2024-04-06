N, A, B = map(int, input().split())

D = list(map(int, input().split()))
x = [d_i % (A + B) for d_i in D]

x = sorted(x)

max_ = max(x)

if 0 < max_ and max_ < A + 1:
    print("Yes")
else:
    print("No")
