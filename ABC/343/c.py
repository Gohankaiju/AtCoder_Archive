n = int(input())

a = 1 * 10 ** 6
for i in range(a):
    tmp = a - i
    s = str(tmp**3)
    if(s == s[::-1]):
        if(tmp**3 <= n):
            print(s)
            exit()
print("0")
