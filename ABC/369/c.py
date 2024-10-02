from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

ans = 1
before_diff = 0
tmp = 0

# 部分列が等差数列となる組の数を数える
for i in range(1, n):
    diff = A[i-1] - A[i]
    if diff == before_diff:
        tmp += 1
        ans += tmp + 1
    else:
        before_diff = diff
        tmp = 1
        ans += tmp + 1
    # print(f"ans: {ans}, diff: {diff}, tmp: {tmp}")

print(ans)


