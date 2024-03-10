N = int(input().split())

A = list(map(int, input().split()))

# 全部 XOR した値（ニム和）を求める

XOR_Sum = A[0]

for i in range(1, N):
    XOR_Sum = XOR_Sum ^ A[i]

if XOR_Sum >= 1:
    print("First")
else:
    print("Second")

"このコードはニムゲームと呼ばれるゲームの勝敗を判断するためのものです。"
"XOR_Sum = XOR_Sum ^ A[i]という行は、XOR演算（排他的論理和）を行っています。"
"これはニム和として知られ、ニムゲームの勝敗を決める鍵となります。"

"XOR演算は、二進数での各桁を比較して、異なっている場合は1、同じ場合は0を返します。"
"例えば、二進数の1010と1001をXOR演算すると、0011になります。"

"このコードでのXOR演算は、石の山の数Nに対して、最初の山の石の数A[0]から始めて、"
"残りの各山A[i]（iは1からN-1まで）の石の数とXORを取っていきます。"
"すべての山についてXORを取った結果がXOR_Sumになります。"

"ニムゲームの理論によると、すべての山の石の数のXORを取った結果（ニム和）が0でなければ、"
"先手が勝つ戦略が存在します。それに対して、ニム和が0であれば、後手が勝つ戦略が存在します。"

"したがって、このコードでは全ての山の石の数に対してXORを取り、"
"その結果が0より大きければ（ニム和が0でなければ）「First」を、ニム和が0であれば"
"「Second」を出力しています。これは、それぞれ先手勝ち、後手勝ちを意味しています。"
