def f(n):
    return 0 if n == 1 else f(n // 2) + f((n + 1) // 2) + n


print(f(int(input())))
