from collections import defaultdict

s = input()
t = input()
X = []
diff = defaultdict(int)

S = list(s)
T = list(t)

# print(ord("a")+ord("s"))
# print(chr(ord("a")+1))

for i in range(len(S)):
    if S[i] != T[i]:
        diff[i] = ord(T[i]) - ord(S[i])

# print(diff)
print(len(diff))
atomawashi = []       
for dic in diff:
    if diff[dic] > 0:
        atomawashi.append(dic)
    else:
        S[dic] = T[dic]
        print("".join(S))

atomawashi.reverse()
for at in atomawashi:
    S[at] = T[at]
    print("".join(S))