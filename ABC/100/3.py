from collections import defaultdict

s = input()
n = len(s)
T = "ATCG"
max_length = 0

for i in range(n):
    if s[i] in T:
        r = i+1
        while r < n and s[r] in T:
            r += 1
        max_length = max(max_length, r-i)

print(max_length)