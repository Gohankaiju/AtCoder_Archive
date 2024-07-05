import sys

daily_ship = {}
ship_list = {}
waiting = {}

class Order:
    def __init__(self, id, c, k):
        self.id = id
        self.c = c
        self.k = k

def detect_order(line):
    parts = line.split()
    return parts if parts[0] == "ORDER" else None

def detect_cancel(line):
    parts = line.split()
    return parts if parts[0] == "CANCEL" else None

def detect_ship(line):
    parts = line.split()
    return parts if parts[0] == "SHIP" else None

def process(i, lines, time, M):
    B, C, K = lines[i].split()
    K = int(K)

    od = Order(B, C, K)

    item_name = []
    item_num = []
    for idx in range(i+1, (i+1) + K):
        x, y = lines[idx].split()
        item_name.append(x)
        item_num.append(int(y))

    if C in daily_ship:
        if daily_ship[C] + sum(item_num) > M:
            print(f"{time} Ordered {B} Error: the number of available shipments has been exceeded.")
            return 0
        else:
            daily_ship[C] += sum(item_num)
            if C not in ship_list:
                ship_list[C] = []
            ship_list[C].append(od)
            waiting[B] = od
    else:
        daily_ship[C] = sum(item_num)
        ship_list[C] = [od]
        waiting[B] = od

    print(f"{time} Ordered {B}")
    return 0

def main(lines):
    N, M, D = map(int, lines[0].split())
    prd_num = lines[1].split()
    daily_flag = list(map(int, lines[2].split()))
    Q = int(lines[3])

    for i, line in enumerate(lines):

        if detect_order(line):
            time = detect_order(line)[1]
            process(i+1, lines, time, M)

        if detect_cancel(line):
            canceled_time = detect_cancel(line)[1]
            canceled_code = lines[i+1]
            print(f"{canceled_time} Canceled {canceled_code}")
            if canceled_code in waiting:
                tmp_od = waiting[canceled_code]
                tmp_num = tmp_od.k
                tmp_date = tmp_od.c
                daily_ship[tmp_date] -= tmp_num
                if daily_ship[tmp_date] == 0:
                    del daily_ship[tmp_date]
                ship_list[tmp_date].remove(tmp_od)
                if len(ship_list[tmp_date]) == 0:
                    del ship_list[tmp_date]
                del waiting[canceled_code]

        if detect_ship(line):
            ship_time = detect_ship(line)[1]
            ship_date = ship_time.split('T')[0]
            if ship_date in ship_list:
                shipping_orders = ship_list[ship_date]
                print(f"{ship_time} Shipped {len(shipping_orders)} Orders")
                tmp_od = ship_date
                shipped_list = []
                for id in shipping_orders:
                    shipped_list.append(id.id)
                print(*shipped_list, sep = ' ')
                del ship_list[ship_date]
                del daily_ship[ship_date]


if __name__ == '__main__':
    lines = [line.rstrip('\r\n') for line in sys.stdin]
    main(lines)