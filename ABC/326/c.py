n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
diff = [0]*n
sum = [0]*n

for i in range(n-1):
    diff[i] = a[i+1] - a[i]

print(a)
print(diff)

for i in range(1, n):
    sum[i] = sum[i-1] + diff[i-1]
print(sum)

for i in range(n-1):
    if sum[i] > m:
        print(i-1)
        exit()

print()


