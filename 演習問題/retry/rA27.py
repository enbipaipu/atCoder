def GCD(A, B):
    big = max(A, B)
    small = min(A, B)
    remainder = big % small

    if remainder == 0:
        return 0

    while remainder != 0:
        big = small
        small = remainder
        remainder = big % small
    return small


A, B = map(int, input().split())

print(GCD(A, B))
