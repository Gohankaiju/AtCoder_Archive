n = int(input())
goods = [list(map(int, input().split())) for _ in range(n)]

# goodsをコピーして、片方をxで、もう片方をyでソートする
goods_x_sorted = sorted(goods)
goods_y_sorted = sorted(goods, key=lambda x: x[1])

# 中央値の計算
if n % 2 != 0:
    door_in = goods_x_sorted[n//2][0]
    door_out = goods_y_sorted[n//2][1]
else:
    door_in = (goods_x_sorted[n//2 - 1][0] + goods_x_sorted[n//2][0]) // 2
    door_out = (goods_y_sorted[n//2 - 1][1] + goods_y_sorted[n//2][1]) // 2

ans = 0
for i in range(n):
    x, y = goods[i]
    ans += abs(x - door_in) + abs(y - x) + abs(door_out - y)
print(ans)
