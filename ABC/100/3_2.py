s = input()
T = "ATCG"
n = len(s)
ans = 0
current_length = 0

for i in range(n):
    if s[i] in T:
        current_length += 1
        ans = max(ans, current_length)
    else:
        current_length = 0

print(ans)
