N = int(input())


def isPalindrome(x):
    return False if x < 0 else str(x) == str(x)[::-1]


R = int(N ** (1 / 3)) + 1
for s in reversed(range(1, R + 1)):
    if s == 1:
        print(1)
        break
    if isPalindrome(s**3) and s ** 3 <= N:
        print(s**3)
        break
