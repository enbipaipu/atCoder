Q = int(input())


def isPrime(num):
    LIMIT = int(num**0.5)
    for t in range(2, LIMIT + 1):
        if num % t == 0:
            return False
    return True


for _ in range(Q):
    X = int(input())
    print("Yes" if isPrime(X) else "No")
