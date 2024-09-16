from itertools import product

def isvalid(s):
    score = 0
    for c in s:
        if c == "(":
            score+=1
        else:
            score -= 1
        
        if score < 0:
            return False
    return score == 0

N = int(input())
for s in product(['(',')'], repeat=N): # '('と')'の組み合わせの長さがNのlistを作る
    print(s)
    if isvalid(s):
        print(*s, sep='')