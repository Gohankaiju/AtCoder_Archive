s = input()
l = len(s)

dp = [[[0] * 2 for _ in range(3)] for _ in range(l + 1)]
dp[0][0][0] = 1  

for i in range(l):
    for j in range(3):
        for k in range(2):
            if dp[i][j][k] > 0:
                dp[i + 1][0][0] += dp[i][j][k]
                if s[i] != 'o':
                    if j < 2:
                        dp[i + 1][j + 1][1] += dp[i][j][k]

ans = 0
for j in range(3):
    ans += dp[l][j][0]
    ans += dp[l][j][1]

print(ans)
