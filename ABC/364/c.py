n, x, y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)    
B.sort(reverse=True)
tmp = 0
max_a = n
max_b = n
for i, a in enumerate(A):
    if tmp + a > x:
        max_a = i+1
        break
    tmp += a

tmp = 0
for i, b in enumerate(B):
    if tmp + b > y:
        max_b = i+1
        break
    tmp += b

print(min(max_a, max_b))



