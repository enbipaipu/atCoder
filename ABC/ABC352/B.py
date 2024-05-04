s = input()
t = input()

ptr_s, ptr_t = 0, 0
ans = []

while ptr_s < len(s) and ptr_t < len(t):
    if s[ptr_s] == t[ptr_t]:
        ans.append(ptr_t + 1)
        ptr_s += 1

    ptr_t += 1


[print(a) for a in ans]
