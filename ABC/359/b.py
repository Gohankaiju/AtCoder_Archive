def count_valid_colors(N, A):
    count = 0
    for i in range(1, N + 1):
        first_index = A.index(i)
        second_index = A.index(i, first_index + 1)
        if second_index - first_index == 2:
            count += 1
    return count

N = int(input())
A = list(map(int, input().split()))

result = count_valid_colors(N, A)

print(result)