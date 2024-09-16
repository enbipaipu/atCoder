## not
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x):
    num = 0  # 何個切れたか
    pre = 0  # 前回の切れ目
    for i in range(N):
        # x を超えたら切断
        if A[i] - pre >= x:
            num += 1
            pre = A[i]

    # 最後のピースが x 以上なら加算
    if L - pre >= x:
        num += 1

    return (num >= K + 1)

left, right = -1, L+1

while right - left > 1:
    mid = (left + right)//2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)