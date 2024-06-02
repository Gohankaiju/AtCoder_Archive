n, m = map(int, input().split())
bit = list(map(int, input().split()))
get = [0]*m

for i in range(n):
    tabe = list(map(int, input().split()))
    for j in range(m):
        get[j] += tabe[j]

for i in range(m):
    if get[i] < bit[i]:
        print("No")
        exit()
print("Yes")
