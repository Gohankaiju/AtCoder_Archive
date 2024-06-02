from itertools import combinations

def count_valid_key_combinations(N, K, tests):
    # 全ての鍵の組み合わせを作成する
    all_keys = list(range(1, N + 1))
    valid_count = 0

    # 鍵の組み合わせをチェックする関数
    def is_valid_combination(valid_keys):
        valid_keys_set = set(valid_keys)
        for test in tests:
            keys, result = test
            count_valid_keys = sum(1 for key in keys if key in valid_keys_set)
            if result == 'o' and count_valid_keys < K:
                return False
            if result == 'x' and count_valid_keys >= K:
                return False
        return True

    # 全ての可能な正しい鍵の組み合わせを試す
    for r in range(N + 1):
        for valid_keys in combinations(all_keys, r):
            if is_valid_combination(valid_keys):
                valid_count += 1

    return valid_count

# 標準入力を受け取る
N, M, K = map(int, input().split())

tests = []
for _ in range(M):
    data = input().split()
    Ci = int(data[0])
    keys = list(map(int, data[1:1+Ci]))
    result = data[1+Ci]
    tests.append((keys, result))

print(count_valid_key_combinations(N, K, tests))
