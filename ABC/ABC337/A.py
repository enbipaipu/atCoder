N = int(input())

x_result = 0
y_result = 0

for _ in range(N):
    X, Y = input().rstrip().split(" ")
    x_result += int(X)
    y_result += int(Y)

if x_result > y_result:
    print("Takahashi")
elif x_result < y_result:
    print("Aoki")
else:
    print("Draw")
