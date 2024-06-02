from collections import defaultdict

n, m = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(n)]
#print(point)
ans = 0

for i in range(m):
    for j in range(i, m):
        score = 0
        for k in range(n):
            best = max(point[k][i], point[k][j])
            score += best
        
        ans = max(ans, score)
print(ans)



