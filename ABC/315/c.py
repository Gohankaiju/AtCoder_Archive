from collections import defaultdict
n = int(input())
ices = [list(map(int, input().split())) for _ in range(n)]

max_value = 0
ans = 0
for i in range(n):
    ice = ices[i]
    if max_value < ice[1]:
        max_value = ice[1]
        aji1 = ice[0]
        idx = i

# print(f"temp={max_value} {aji1}")
# print(ices)
ices.pop(idx)


for ice in ices:
    if aji1 == ice[0]:
        temp = max_value + ice[1]//2
    else:
        temp = max_value + ice[1]
    # print(temp)
    # print(aji1, ice[0])
    ans = max(ans, temp)


print(ans)

