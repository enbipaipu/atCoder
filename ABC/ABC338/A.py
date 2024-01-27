import re

s = input()
if re.match("[A-Z][a-z]*$", s):
    print("Yes")
else:
    print("No")
