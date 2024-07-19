from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
box = [-1]*(n+1)
ans = 0

for i in range(n):
    a = A[i]
    w = W[i]
    if box[a] == -1:
        box[a] = w
    else:
        ans += min(box[a], w)
        box[a] = max(box[a], w)
        #print(f"a:{a}, w:{w}, ans:{ans}")
print(ans)

