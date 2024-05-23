n = int(input())
kyaku = list(map(int, input().split()))

sm = 0
sm_list = []

for k in kyaku:
    sm += k
    sm_list.append(int(sm))

if(min(sm_list) > 0):
    print(sm)
else:
    print(abs(min(sm_list)) + sm)


