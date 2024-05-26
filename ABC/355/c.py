n, t = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))
row = [0]*n
col = [0]*n
ver1 = 0
ver2 = 0
bingo = False

for i in range(t):
    x = a[i] % n 
    y = a[i] // n

    row[y] += 1
    if row[y] == n:
        bingo = True

    col[x] += 1
    if col[x] == n:
        bingo = True

    if x == y:
        ver1 += 1
        if ver1 == n:
            bingo = True
     
    if x + y == n - 1:
        ver2 += 1
        if ver2 == n:
            bingo = True

    if bingo:
        print(i + 1)
        exit()

print(-1)