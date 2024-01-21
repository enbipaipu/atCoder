n = int(input())
a = input().rstrip().split(" ")
a = [int(s) for s in a]

result = [x for x in a if x != max(a)]

print(max(result))
