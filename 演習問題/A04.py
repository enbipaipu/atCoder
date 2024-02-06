n = int(input())
x = bin(n)[2:]
print("0" * (10 - len(x)) + x)
