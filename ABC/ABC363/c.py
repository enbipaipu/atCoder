N, K = map(int, input().split())
S = sorted(input())

palindrome_count = 0	# 長さKの回文の個数
palindrome_check = [0] * (N - K + 1)	# 長さKの文字列それぞれに対して、回文になっている文字の位置のフラグ
is_palindrome = (1 << (K + 1 >> 1)) - 1	# フラグが回文となる条件
for l in range(N - K + 1):
	for i in range(K + 1 >> 1):
		if S[l + i] == S[l + K - 1 - i]:
			palindrome_check[l] ^= 1 << i
	if palindrome_check[l] == is_palindrome:
		palindrome_count += 1

def toggle(i):	# i番目の文字が@でないなら@に、@なら元の文字に変えた時の差分更新
	global palindrome_count
	for l in range(max(0, i - K + 1), min(i, N - K) + 1):	# S[l, l+K)の回文について更新
		if palindrome_check[l] == is_palindrome:
			palindrome_count -= 1
		flag_index = i - l	# 先頭から見て何文字目か
		opposite = K - 1 - flag_index
		if flag_index > opposite:
			flag_index, opposite = opposite, flag_index
		if S[l + flag_index] == S[l + opposite]:
			palindrome_check[l] ^= 1 << flag_index
		if palindrome_check[l] == is_palindrome:
			palindrome_count += 1

# swapした時の差分更新を高速に行う
def swap(i, j):
	toggle(i)
	toggle(j)
	S[i], S[j] = S[j], S[i]
	toggle(i)
	toggle(j)

# next_permutationを求める
def next_permutation(S):
	for i in range(N - 1)[::-1]:
		if S[i] >= S[i + 1]:
			continue
		for j in range(i + 1, N)[::-1]:
			if S[i] < S[j]:
				break
		swap(i, j)
		for l in range(i + 1, N):
			r = N + i - l
			if l >= r:
				break
			swap(l, r)
		return True
	return False

ans = 1 if palindrome_count == 0 else 0
while next_permutation(S):
	if palindrome_count == 0:
		ans += 1
print(ans)