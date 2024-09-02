# ライブラリ
import more_itertools

# 標準入力
N, K = map(int, input().split())
S = input()

ans = 0
# 全ての並び替えでループさせる
for s in more_itertools.distinct_permutations(S):
  # 回文が存在しない判定フラグ
  ok = True
  # i~i+Kが回文かどうかの判定
  for i in range(N-K+1):
    permutate = True
    for j in range(K//2):
      if s[i+j] != s[i+K-j-1]:
        permutate = False
    if permutate:
      ok = False
  
  if ok:
    ans += 1
print(ans)