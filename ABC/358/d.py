N, M = map(int, input().split())
boxes = list(map(int, input().split()))
hito = list(map(int, input().split()))

boxes.sort()
hito.sort()
i = 0
ans = 0
for box in boxes:
    if box >= hito[i]:
        i += 1
        ans += box
        
    if i == M:
        print(ans)
        exit()

print(-1)