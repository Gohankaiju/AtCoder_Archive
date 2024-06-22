n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

created_num = []

for i in range(1<<n):
    tmp = 0
    #print(i)
    for sf in range(n):
        if 1 & i >> sf == 1:
            tmp += n_list[sf]
    created_num.append(tmp)

for m_num in m_list:
    if m_num in created_num:
        print("yes")
    else:
        print("no")