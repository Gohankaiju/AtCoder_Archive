s1, s2 = map(int, input().split())
t1, t2 = map(int, input().split())

bias = 0
if ((s1+s2) % 2 != (t1+t2) % 2):
    bias = 1

tate = abs(s2 - t2) 
if tate + bias < abs(s1 - t1):
    yoko = abs(s1 - t1)
else:
    yoko = 0
#print(f"tate = {tate}, yoko = {yoko}")
ans = tate + yoko
print(ans)

