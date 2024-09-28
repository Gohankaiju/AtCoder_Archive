from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    q = list(map(int, input().split()))
    q_num = q[0]
    if q_num != 3:
        x = q[1]
    if q_num == 1:
        d[x] += 1
    elif q_num == 2:
        d[x] -= 1
        if d[x] == 0:
            del d[x]
    elif q_num == 3:
        print(len(d))

