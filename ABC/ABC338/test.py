import re

s = input()
if re.match("[A-Z]", s):
    print("ok")
else:
    print("false")
