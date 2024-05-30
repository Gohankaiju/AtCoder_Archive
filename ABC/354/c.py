n = int(input())

card = []
for i in range(n):
    x, y = map(int, input().split())
    card.append((x, y, i+1))

s_card = sorted(card, key=lambda x: x[1])
#print(s_card)
max = 0
ans = []
for i in range(n):
    c = s_card[i]
    if max < c[0]:
        ans.append(c[2])
        #print(f"ans={ans}")
        max = c[0]
    else:
        continue

print(len(ans))
print(*sorted(ans))
