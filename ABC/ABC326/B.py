n = int(input())

if n >= 100 and n <= 919:
    for s in range(n, 920):
        x = str(s)
        if int(x[0]) * int(x[1]) == int(x[2]):
            print(x)
            break