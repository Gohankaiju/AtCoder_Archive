from collections import defaultdict

while True:
    ans = 0
    n, x = map(int, input().split())
    if (n == x == 0):
        exit()
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    ans += 1
                    print(f"{i} {j} {k}")
    print(ans)


