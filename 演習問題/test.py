import time

start0 = time.time()
c = 9
for s in range(10**6):
    c = 0

goal0 = time.time()
print(goal0 - start0)
start1 = time.time()
a = 9
for s in range(10**7):
    a = 0

goal1 = time.time()

print(goal1 - start1)

start2 = time.time()

b = 9
for s in range(10**8):
    b = 0

goal2 = time.time()
print(goal2 - start2)
