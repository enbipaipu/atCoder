N, A, B = map(int, input().split())

A1 = N // B
A2 = N % B

A3 = A2 // A

if (A1 + A3) % 2 == 1:
    print("First")
else:
    print("Second")
