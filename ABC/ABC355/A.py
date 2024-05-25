ans = {1, 2, 3}

A, B = map(int, input().split())

if A == B:
    print(-1)
else:
    for s in ans:
        if s != A and s != B:
            print(s)
