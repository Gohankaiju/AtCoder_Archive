import string
from collections import defaultdict

n = int(input())
s = input()

al = list(string.ascii_lowercase)
ans = defaultdict(int)
l = 0

while l < n:
    r = l + 1
    while r < n and s[l] == s[r]:
        r += 1
        
    ans[s[l]] = max(ans[s[l]], r - l)
    l = r

result = 0

for key in ans:
    result += ans[key]

print(result)
