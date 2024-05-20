s = input()
n = len(s)
dict = {}
ans = 0
dub = 0

for c in s:
    if c in dict:
        dict[c] += 1
    else:
        dict[c] = 1
for k in dict.keys():
    if dict[k] > 1:
        dub += (dict[k] * (dict[k] - 1)) / 2
if dub != 0:
    print((int(n * (n - 1) / 2 - dub) + 1))
    exit()
print(int(n * (n - 1) / 2 - dub))


