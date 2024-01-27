n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def only(lis: list, Q: list):
    result = []
    for s in range(n):
        result.append(Q[s] // lis[s])
    return min(result)


def sa(A, B):
    new_q = []
    lis = []
    if A < B:
        lis = a
        for s in range(n):
            new_q.append(q[s] - (lis[s] * (A - 1)))
    else:
        lis = b
        for s in range(n):
            new_q.append(q[s] - (lis[s] * (B - 1)))
    return [new_q, lis]


only_A = only(a, q)
only_B = only(b, q)

result1 = sa(only_A, only_B)

result = only(result1[1], result1[0])

print(result)
