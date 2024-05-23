s = input()
t = input()

dic = {"A":1, "B":2, "C":3, "D":4, "E":5}

if abs(dic[s[0]] - dic[s[1]]) == 1 or abs(dic[s[0]] - dic[s[1]]) == 4:
    if abs(dic[t[0]] - dic[t[1]]) == 1 or abs(dic[t[0]] - dic[t[1]]) == 4:
        print("Yes")
    else:
        print("No")
else:
    if abs(dic[t[0]] - dic[t[1]]) == 1 or abs(dic[t[0]] - dic[t[1]]) == 4:
        print("No")
    else:
        print("Yes")
