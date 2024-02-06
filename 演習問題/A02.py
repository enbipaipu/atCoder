n, x = map(int, input().split())

s = list(input().split())

t = [y for y in s if y == str(x)]

if t:
    print("Yes")
else:
    print("No")
