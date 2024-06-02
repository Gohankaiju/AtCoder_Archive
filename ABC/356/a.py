n, l, r = map(int, input().split())

lan = [i for i in range(1,n+1)]

sublan = lan[l-1:r][::-1]
#print(sublan)
lan[l-1:r] = sublan
print(*lan)

