import sys
import itertools

def count_tiles(n, m):
    total = n * m
    #タイルの総数が奇数の場合、同じ数で塗ることはできない
    if total % 2 != 0:
        return 0
    #一色ごとの塗るタイルの数
    falf = total // 2
    #計算量削減のため動的計画法を使用
    dp = [[0] * (falf + 1) for _ in range(total + 1)]
    #dp[n枚のタイルの中から][n枚を選ぶ] = a通り
    dp[0][0] = 1

    for i in range(1, total + 1):
        for j in range(0, falf + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            #print(f"{i}, {j} = {dp}")
    result = dp[total][falf]

    return result

def main():
    try:
        n, m = map(int, input().split())
        
        if n < 0 or m < 0:
            raise ValueError
        
        result = count_tiles(n, m)
        #下9桁を出力
        print(f"{result % 1000000000:09d}")
        
    except Exception as e:
        sys.exit(100)

if __name__ == "__main__":
    main()