n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)


amasa = 0
syopa = 0
amasa_min = 0
syopa_min = 0

print(n, x, y, a, b)

for i in range(n):
    amasa += a[i]
    amasa_min += 1
    if amasa > x:
        break

for j in range(n):
    syopa += b[i]
    syopa_min += 1
    if syopa > y:
        break

print(min(amasa_min, syopa_min))



