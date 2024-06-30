S = input()

has_R = False
result = True

for t in S:
    if t == "M":
        if has_R is True:
            result = False
    elif t == "R":
        has_R = True

print("No" if result else "Yes")
