n, m = map(int, input().split())
day = input()
ans = 0
ans_list = []
ans_list.append(0)
nowm = m

for d in day:
    a = int(d)
    if a == 0:
        ans_list.append(ans)
        ans  = 0
        nowm = m
    if a == 1:
        if nowm > 0:
            nowm -= 1
        else:
            ans += 1
    if a == 2:
            ans += 1

print(max(max(ans_list), ans))