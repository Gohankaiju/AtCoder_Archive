from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()
else:
    mini = 0
    maxi = max(A)
    ans = 0
    while mini <= maxi:
        mid = (mini + maxi) // 2
        sum = 0
        for a in A:
            sum += min(a, mid)
        if sum > M:
            maxi = mid - 1
        else:
            mini = mid + 1
            ans = max(ans, mid)
print(ans)

