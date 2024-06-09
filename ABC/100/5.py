import itertools
import math
from collections import defaultdict

n = map(int, input().split())
s = input()
ans = 0

for i in range(10): 
    for j in range(10):
        for k in range(10):
            now = str(i*100 + j*10 + k).zfill(3)
            itr = 0
            for keta in s:
                if keta == now[itr]:
                    itr += 1
                if itr >= 3:
                    ans += 1
                    break

print(ans)
            




