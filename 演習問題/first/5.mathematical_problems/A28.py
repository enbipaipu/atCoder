def calculation(st, num, ans):
    num = int(num)
    if st == "+":
        ans += num
    elif st == "-":
        ans -= num
    else:
        ans *= num
    return ans


N = int(input())

ans = 0

for s in range(N):
    T, A = input().split()
    ans = calculation(T, A, ans)
    if ans < 0:
        ans += 10000
    ans %= 10000
    print(ans)
