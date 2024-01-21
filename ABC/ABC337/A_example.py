N = int(input())

TakahashiScore = 0  # チーム高橋の合計得点
AokiScore = 0  # チーム青木の合計得点

for i in range(N):
    X, Y = map(int, input().split())

    # それぞれのチームに得点をプラスする
    TakahashiScore += X
    AokiScore += Y
# 合計得点の大小に従って結果を出力
if TakahashiScore > AokiScore:
    print("Takahashi")
elif TakahashiScore < AokiScore:
    print("Aoki")
else:
    print("Draw")
