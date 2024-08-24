N = int(input())
H = list(map(int, input().split()))
T = 0

for h in H:
    if T % 3 == 1:
        h-=1
        T+=1
        if h <= 0:
            continue
        h-=3
        T+=1
        if h <= 0:
            continue
    elif T % 3 == 2:
        h-=3
        T+=1
        if h <= 0:
            continue
    
    T += (h//5) * 3
    diff = h % 5

    if diff <= 2:
        T+=diff
    elif diff >= 3:
        T+=3
    
print(T) 