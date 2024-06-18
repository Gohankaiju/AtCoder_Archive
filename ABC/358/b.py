n, a = map(int, input().split())
t = list(map(int, input().split()))

now = 0

for i in range(n):
    if i == 0:
        now += t[i]
        now += a
    else:
        if t[i] > now:
            now = t[i] + a
        else:
            now += a
    
    print(now)

