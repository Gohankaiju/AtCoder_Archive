n, k = map(int, input().split())
vc = list(map(int, input().split()))
sum = k*(k+1)//2
#print(sum)

a = list(set(vc))

for x in a:
    if x <= k:
        sum -= x

print(sum)
