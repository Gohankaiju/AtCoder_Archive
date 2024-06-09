from collections import defaultdict

n, m = map(int, input().split())
fin = list(map(int, input().split()))
ans = 0
for f in fin:
        m -= f
        if m < 0:
            break
        else:
            ans += 1

print(ans)
    

