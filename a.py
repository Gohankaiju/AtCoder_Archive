s = input()
code = input()

if code[2] == "X":
    tmp = code[0:2]
    cnt = 0
    for c in s.upper():
        if c == tmp[cnt]:
            cnt += 1
        if cnt == 2:
            print("Yes")
            exit()
else:
    cnt = 0
    for c in s.upper():
        if c == code[cnt]:
            cnt += 1
        if cnt == 3:
            print("Yes")
            exit()
print("No")
