from collections import defaultdict
from itertools import permutations

N = int(input())
adj1 = [[0] * N for _ in range(N)]
adj2 = [[0] * N for _ in range(N)]
M1 = int(input())
for _ in range(M1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj1[a][b] = 1
    adj1[b][a] = 1

M2 = int(input())
for _ in range(M2):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj2[a][b] = 1
    adj2[b][a] = 1

# print(adj1)
# print(adj2)

A = []
for i in range(N-1):
    row = list(map(int, input().split()))
    A.append([0] * (i + 1) + row)

# print(A)

ans = 10**9
for p in permutations(range(N)):
    # print(p)
    cost = 0
    for i in range(N):
        for j in range(i+1, N):
            if adj1[p[i]][p[j]] ^ adj2[i][j]:
                # print(f"i {i} j {j} {adj1[p[i]][p[j]]} {adj2[i][j]}")
                cost += A[i][j]
    ans = min(ans, cost)

print(ans)
