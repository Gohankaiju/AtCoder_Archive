from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 2*10**9
for i in range(0, k+1):
    ans = min(ans, A[i+(n-k)-1] - A[i])
print(ans)
