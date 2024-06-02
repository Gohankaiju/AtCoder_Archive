n, q = map(int, input().split())
s = input()
dub = [0]*(n-1)

cnt = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        dub[i] += 1

presum = [0]*(n)
for i in range(1, n):
    presum[i] = presum[i-1] + dub[i-1]

#print(dub)
#print(presum)

for i in range(q):
    l, r = map(int, input().split())
    print(presum[r-1] - presum[l-1])