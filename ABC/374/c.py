from collections import defaultdict
import itertools

n = int(input())
K = list(map(int, input().split()))
K_sum = sum(K)
ans = 10**9

for i in range(1, 21):
    comb = list(itertools.combinations(K, i))


    for c in comb:
        # print(c)
        group = sum(c)
        if group >= K_sum - group:
            ans = min(ans, sum(c))

print(ans)