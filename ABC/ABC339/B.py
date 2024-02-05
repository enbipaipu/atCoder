h, w, n = map(int, input().split())

dic = {y: {x: "." for x in range(w)} for y in range(h)}

now_y = 0
now_x = 0
direction: int = 0
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]


for _ in range(n):

    if now_x == -1:
        now_x = w - 1
    if now_x == w:
        now_x = 0
    if now_y == -1:
        now_y = h - 1
    if now_y == h:
        now_y = 0

    if dic[now_y][now_x] == ".":
        dic[now_y][now_x] = "#"
        direction += 90
    else:
        dic[now_y][now_x] = "."
        direction -= 90
    direction2 = int((abs(direction % 360) / 90) % 4)

    now_y = now_y + dire[direction2][0]
    now_x = now_x + dire[direction2][1]

for s in range(h):
    print("".join(dic[s].values()))
