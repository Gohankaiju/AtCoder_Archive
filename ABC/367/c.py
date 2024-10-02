from collections import defaultdict

N, K = map(int, input().split())
R = list(map(int, input().split()))

# 再起によって列挙
def f(i, A):
    if i == N:
        if sum(A) % K == 0:
            print(" ".join(map(str, A)))
    else:
        for j in range(1, R[i] + 1):
            A.append(j)
            f(i + 1, A)
            A.pop()

f(0, [])