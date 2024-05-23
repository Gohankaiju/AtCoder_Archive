h, w ,n = map(int, input().split())
move = input()
mp = [list(input()) for _ in range(h)]
ans = 0

for j in range(1, h-1):
    for k in range(1, w-1):
        st = [j, k]
        ck = True
        if(mp[st[0]][st[1]] == "#"):
                ck = False
        for m in move:
            if m == "L":
                if st[1] > 0:
                    st[1] -= 1
                else:
                    ck = False
                    break
            elif m == "R":
                if st[1] < w-1:
                    st[1] += 1
                else:
                    ck = False
                    break
            elif m == "U":
                if st[0] > 0:
                    st[0] -= 1
                else:
                    ck = False
                    break
            elif m == "D":
                if st[0] < h-1:
                    st[0] += 1
                else:
                    ck = False
                    break
            if(mp[st[0]][st[1]] == "#"):
                ck = False
                break
        if ck:
            ans += 1

print(ans)