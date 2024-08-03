from collections import defaultdict

n = int(input())
x = 3**n
s = [["#"] *3*n for _ in range(3*n)]
print(s)
print(0%1)

def split(i, j, temp, s):
    grid = temp // 3
    if grid == 0:
        pass
    else:
        print(f"grid={grid}")
        for k in range(temp):
            for l in range(temp):
                if k%grid == 1 and l%grid == 1:
                    s[i+k][j+l] = "."
                else:
                    s[i+k][j+l] = "#"
    return s


temp = x
while temp >= 3:
    temp = temp // 3
    print(f"temp={temp}")
    for i in range(3):
        for j in range(3):
            s = split(i*temp, j*temp, temp, s)
    

print(s)


