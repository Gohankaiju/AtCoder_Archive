from collections import defaultdict


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))



ab = (b[0] - a[0])**2 + (b[1] - a[1])**2

ac = (c[0] - a[0])**2 + (c[1] - a[1])**2

bc = (c[0] - b[0])**2 + (c[1] - b[1])**2



if ab + ac == bc:
    print("Yes")
    exit
elif ab + bc == ac:
    print("Yes")
    exit
elif ac + bc == ab:
    print("Yes")
    exit
else:
    print("No")
    

    
