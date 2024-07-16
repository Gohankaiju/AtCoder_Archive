n = int(input())

flex = 0
summ = 0
nums = [[0]*2 for _ in range(n)]
#print(nums)

for i in range(n):
    l, r = map(int, input().split())
    nums[i][0] = l
    nums[i][1] = r
    summ += l
    flex += (r -l)

if(summ > 0):
    print("No")
    exit()
else:
    if((summ * (-1)) <= flex):
        print("Yes")
    else:
        print("No")
        exit()

ans = []
add = summ * (-1)
for num in nums:
    l = num[0]
    r = num[1]
    if(add > 0):
        if add > r-l:
            ans.append(r)
            add -= (r-l)
        else:
            ans.append(l+add)
            add = 0
    else:
        ans.append(l)
        add = 0

print(*ans)
#print(sum(ans))
    



