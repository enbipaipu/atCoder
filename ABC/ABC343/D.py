from collections import defaultdict

# 入力を受け取る
n, t = map(int, input().split())

# スコアを管理するリスト
score = [0] * n

# 各スコアの出現回数を管理する辞書
mp = defaultdict(int)
mp[0] = n

# クエリを処理する
for _ in range(t):
    a, b = map(int, input().split())
    a -= 1  # 0-indexedに調整

    # スコアの更新前にそのスコアの出現回数を減らす
    mp[score[a]] -= 1
    if mp[score[a]] == 0:
        del mp[score[a]]

    # スコアを更新
    score[a] += b

    # 更新後のスコアの出現回数を増やす
    mp[score[a]] += 1

    # 異なるスコアの数を出力
    print(len(mp))
