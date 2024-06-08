S = input()

big = sum(map(str.islower, S))
small = sum(map(str.isupper, S))

if big <= small:
    print(S.upper())
else:
    print(S.lower())
