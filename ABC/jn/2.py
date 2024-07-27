n = int(input())
Garden = list(map(int, input().split()))

max_value = max(Garden)
second_max_value = max(x for i, x in enumerate(Garden) if i != Garden.index(max_value))

for i in range(n):
    if Garden[i] == max_value:
        print(second_max_value)
    else:
        print(max_value)