N = int(input())

lis = [N]
ans = 0

while len(lis) > 0:
    num = max(lis)
    lis.remove(num)  # numをリストから削除
    ans += num
    A = num // 2
    B = num - A

    if A > 1:  # Aが1以上の場合のみ追加
        lis.append(A)
    if B > 1:  # Bが1以上の場合のみ追加
        lis.append(B)

print(ans)
