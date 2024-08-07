from collections import defaultdict

n = int(input())
ans = 0
val = set()
for _ in range(n):
    a = input()
    if (a in val) == False:
        ans += 1
    val.add(a)
    val.add(a[::-1])

print(ans)

