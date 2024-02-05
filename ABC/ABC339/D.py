Vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(input())
s = [input() for _ in range(n)]

grid = {y: {u: t for u, t in enumerate(x)} for y, x in enumerate(s)}


def move_pos(position, y, x):
    new_position = (position[0] + y, position[1] + x)

    if grid[new_position[0]][new_position[1]] == "#":
        return position
    return new_position


player = [(y, x) for y, X in enumerate(s) for x, T in enumerate(X) if T == "p"]

player1, player2 = player


for X in grid:
    print(grid[X])

print(player1, player2)
