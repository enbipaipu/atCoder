A = []
while True:
    t = int(input())
    A.append(t)
    if t == 0:
        break

for s in reversed(A):
    print(s)
