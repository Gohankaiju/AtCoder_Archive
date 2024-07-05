k = int(input())
a = []

for i in range(1<<10):
    x = 0
    for j in range(9, -1, -1):
        if(i>>j&1):
            x = x*10 + j
    if x == 0:
        continue
    a.append(x)

a.sort()
#print(a)
print(a[k-1])
