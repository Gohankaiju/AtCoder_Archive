N,Q = map(int, input().split())
A = [(i + 1, 0) for i in range(N)][::-1]
#print(A)

for _ in range(Q):
    a, b = input().split()
    if a == "1":
        x,y = A[-1]
        if b == "R": x += 1
        if b == "L": x -= 1
        if b == "U": y += 1
        if b == "D": y -= 1
        A.append((x,y))
    else:
        print(*A[-int(b)])