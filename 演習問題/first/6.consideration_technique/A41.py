N = int(input())

S = input()

ans = False

for i in range(0, N - 2):
    if S[i] == "R" and S[i + 1] == "R" and S[i + 2] == "R":
        ans = True
    if S[i] == "B" and S[i + 1] == "B" and S[i + 2] == "B":
        ans = True

if ans is True:
    print("Yes")
else:
    print("No")
