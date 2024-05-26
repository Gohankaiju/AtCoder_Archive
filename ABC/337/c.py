n = int(input())
p = list(map(int, input().split()))
s = [-1]*(n+1)

for i in range(n):
    num = p[i]
    if num == -1:
        tmp = i+1
        s[0] = i+1
    else:
        s[num] = i+1

ans = []
ans.append(tmp)

for i in range(n-1):
    ans.append(s[tmp])
    tmp = s[tmp]

print(*ans)

