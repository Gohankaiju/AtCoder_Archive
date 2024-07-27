from collections import defaultdict

n = int(input())
flag = 0
for i in range(n):
    s = input()
    if s == "sweet":
        if flag == 0:
            flag = 1
        else:
            if i == n-1:
                break
            else:
                print("No")
                exit()
    else:
        flag = 0

print("Yes")

