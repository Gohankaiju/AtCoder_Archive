from collections import defaultdict

n = int(input())

s = "Takahashi"
ans = 0
for i in range(n):
    ss = input()
    #print(ss)
    if ss == s:
        ans += 1
print(ans)
