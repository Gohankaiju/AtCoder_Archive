from collections import defaultdict

n, q = map(int, input().split())
s = input()

ans = 0

for i in range(n-2):
    tmp = s[i:i+3]
    # print(tmp)
    if tmp == "ABC":
        ans += 1

# print(ans)

S = []
for i in range(n):
    S.append(s[i])

for _ in range(q):
    t, x = map(str, input().split())
    itr = int(t) - 1
    s_old = "".join(S)
    S[itr] = x    
    # print(S)
    # print(f"itr: {itr}")
    # print("".join(S))
    # print("__________________________")
    for i in range(itr-2, itr+1):
        # print(f"i: {i}")
        if i >= 0 and i <= n-2:
            before_temp = s_old[i:i+3]
            temp = "".join(S[i:i+3])
            # print(f"before_temp: {before_temp} temp: {temp}")
            if (temp == "ABC") ^ (before_temp == "ABC"):
                # print("数が変わります")
                if temp == "ABC":
                    ans += 1
                else:
                    ans -= 1
    print(ans)

# print(f"last ans: {ans}")