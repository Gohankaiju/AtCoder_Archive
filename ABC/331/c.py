from collections import defaultdict

n = int(input())
r = list(map(int, input().split()))
s = set()
d = defaultdict(int)
upper_sum = defaultdict(int)
for i in r:
    d[i] += 1
    s.add(i)
s = sorted(list(s))
#print(s)

upper_sum[s[0]] = sum(r) - d[s[0]] * s[0]
for i in range(1, len(s)):
    upper_sum[s[i]] = upper_sum[s[i-1]] - s[i] * d[s[i]]

ans = []
for rr in r:
    ans.append(upper_sum[rr])

print(*ans)
#print(f"{d} {upper_sum}")


