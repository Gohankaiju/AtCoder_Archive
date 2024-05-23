n, t = map(int, input().split())
man = [0 for _ in range(n)]
dic = {}
dic[0] = n
for _ in range(t):
    a, b = map(int, input().split())
    dic[man[a-1]] -= 1
    if dic[man[a-1]] == 0:
        dic.pop(man[a-1])
    man[a-1] += b
    if man[a-1] in dic:
        dic[man[a-1]] += 1
    else:
        dic[man[a-1]] = 1
    print(len(dic))

    
    




