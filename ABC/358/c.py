import itertools

n, m = map(int, input().split())
l = [input().split()[0] for _ in range(n)]  

for i in range(1, n + 1):
    for comb in itertools.combinations(l, i):
        ck = [0] * m
        for string in comb:
            for j in range(m):
                if string[j] == 'o':
                    ck[j] = 1
        if all(ck):
            print(i)
            exit()
