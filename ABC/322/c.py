n, m = map(int, input().split())
a = list(map(int, input().split()))

itr = 0
for i in range(1, n+1):
    if i == a[itr]:
        print(0)
        itr += 1
    else:
        print(a[itr] - i)
        
