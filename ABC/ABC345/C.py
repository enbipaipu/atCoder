from collections import defaultdict
S=input()
N=len(S)
ans=0
count=defaultdict(int)
for j in range(N):
  ans+=j-count[S[j]]  # i として選べるのは、j までの文字のうち S[j] と同じでないもの
  count[S[j]]+=1
if max(count.values())>1:
  ans+=1
print(ans)
