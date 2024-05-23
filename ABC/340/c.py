def calculate_total_cost(n):
    # メモ化用の辞書
    memo = {}

    def helper(x):
        # xが1以下の場合、コストは0
        if x <= 1:
            return 0
        # メモに結果が保存されている場合、それを返す
        if x in memo:
            return memo[x]

        # ⌊x/2⌋と⌈x/2⌉を計算
        floor_half = x // 2
        ceil_half = (x + 1) // 2
        
        # 再帰的にコストを計算
        cost = x + helper(floor_half) + helper(ceil_half)
        
        # 結果をメモに保存
        memo[x] = cost
        return cost

    return helper(n)

# 使用例
n = int(input())
print(calculate_total_cost(n))  # 効率化された方法での出力
