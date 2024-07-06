N = int(input())

count = 1

befo = "#"
now = "#"
while count <= N:

    befo = now

    white = ["." * (3 ** (count - 1))] * (3 ** (count - 1))
    now = [
        [befo, befo, befo],
        [befo, white, befo],
        [befo, befo, befo],
    ]
    count += 1

[print(s) for s in now]
