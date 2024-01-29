s = input()

x = s[0].isupper()

y = s[1 : len(s) + 1].islower()


if x and y:
    print("Yes")
elif len(s) == 1 and x:
    print("Yes")
else:
    print("No")
