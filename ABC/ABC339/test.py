dic = {y: {x: x**2 + y for x in range(1, 5)} for y in range(1, 4)}

[print(dic[s][x]) for s in range(1, 4) for x in dic[s]]
