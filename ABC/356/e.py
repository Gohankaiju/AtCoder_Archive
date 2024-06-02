from collections import Counter

def calculate_sum(N, A):
    # 数列の要素ごとの頻度をカウント
    count = Counter(A)
    total_sum = 0
    
    # 各要素について計算
    for x in count:
        for y in count:
            if x <= y:
                total_sum += (x // y) * count[x] * count[y]
            else:
                total_sum += (y // x) * count[x] * count[y]
    
    # 重複を除くために、i < j のペアは2倍されているので、除算する
    return total_sum

# 標準入力からNとAを読み取る
N = int(input())
A = list(map(int, input().split()))
result = calculate_sum(N, A)
print(result)
