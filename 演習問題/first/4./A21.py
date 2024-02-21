# 入力
N = int(input())
P = [None] * (N + 1)
A = [None] * (N + 1)
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

# 動的計画法（LEN は r-l の値)
dp = [[None] * (N + 1) for i in range(N + 1)]
dp[1][N] = 0
for LEN in reversed(range(0, N - 1)):
    for L in range(1, N - LEN + 1):
        r = L + LEN

        # score1 の値（l-1 番目のブロックを取り除くときの得点）を求める
        score1 = 0
        if L >= 2 and L <= P[L - 1] and P[L - 1] <= r:
            score1 = A[L - 1]

        # score2 の値（r+1 番目のブロックを取り除くときの得点）を求める
        score2 = 0
        if r <= N - 1 and L <= P[r + 1] and P[r + 1] <= r:
            score2 = A[r + 1]

        # dp[l][r] を求める
        if L == 1:
            dp[L][r] = dp[L][r + 1] + score2
        elif r == N:
            dp[L][r] = dp[L - 1][r] + score1
        else:
            dp[L][r] = max(dp[L - 1][r] + score1, dp[L][r + 1] + score2)

# 出力
Answer = 0
for i in range(1, N + 1):
    Answer = max(Answer, dp[i][i])
print(Answer)
