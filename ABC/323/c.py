n, m = map(int, input().split())
point = list(map(int, input().split()))
person = [0]*n
best = 0
notsolve = [[] for _ in range(n)]

for i in range(n):
    st = input()
    for j in range(m):
        if st[j] == "o":
            person[i] += point[j]
        else:
            notsolve[i].append(point[j])
    person[i] += i+1
    best = max(best, person[i])


for i in range(n):
    if person[i] >= best:
        print(0)
    else:
        notsolve[i].sort(reverse=True)
        for j in range(len(notsolve[i])):
            person[i] += notsolve[i][j]
            if person[i] >= best:
                print(j+1)
                break

            
        

#print(person)






