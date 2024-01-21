N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

dic = dict()
for i in range(N):
    dic[A[i]] = i
ans_lst = [dic[-2]]
for _ in range(N - 1):
    tail = ans_lst[-1]
    ans_lst.append(dic[tail])
    print(tail, ans_lst)
for i in range(N):
    ans_lst[i] += 1
print(*ans_lst)
