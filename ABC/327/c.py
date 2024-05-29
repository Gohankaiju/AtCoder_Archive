grid = [list(map(int, input().split())) for _ in range(9)]
a = True
jud = set(range(1,10))

for row in grid:
    if set(row) != jud:
        a = False
        break

for col in range(9):
    cols = set(grid[row][col] for row in range(9))
    if cols != jud:
        a = False
        break

for i in range(3):
    for j in range(3):
        cols = set(grid[3*i+k][3*j+l] for k in range(3) for l in range(3))
        if cols != jud:
            a = False
            break

if a:
    print("Yes")
else:
    print("No")