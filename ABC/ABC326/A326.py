n = input().rstrip().split(' ')
n = [int(s) for s in n]
x = n[0]
y = n[1]

if y - x < 3 and y - x > -4:
    print('Yes')
else:
    print('No')