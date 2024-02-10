A, B, D = map(int, input().split())

ans = []
n = 1
while True:
    an = A + (n - 1) * D
    ans.append(an)
    n += 1
    if an == B:
        break

for i in ans:
    print("".join(str(i)))
