h, w = map(int, input().split())
si, sj = map(int, input().split())
s = []
s.append(['#' for _ in range(w+2)])
for _ in range(h):
    temp = input()
    temp = f"#{temp}#"
    s.append(list(temp))
s.append(['#' for _ in range(w+2)])
# print(s)
# print(si, sj)
x = input()

for dic in x:
    if dic == 'U':
        if s[si-1][sj] == '.':
            #print("a")
            si-=1
    if dic == 'D':
        if s[si+1][sj] == '.':
            si+=1
    if dic == 'R':
        if s[si][sj+1] == '.':
            sj+=1
    if dic == 'L':
        if s[si][sj-1] == '.':
            sj-=1
print(si, sj)