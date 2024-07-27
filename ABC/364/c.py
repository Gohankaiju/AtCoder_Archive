n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)


amasa = 0
syopa = 0

for i in range(n):
    menu = a[i]
    amasa += menu
    if amasa > x:
        amasa = i+1
        break

for j in range(n):
    menu = b[i]
    syopa += menu
    if syopa > y:
        syopa = i+1
        break

print(min(amasa, syopa))



