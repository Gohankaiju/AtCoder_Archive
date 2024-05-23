import queue

n = int(input())
s = input()
q = int(input())

len = queue.LifoQueue()
all = "abcdefghijklmnopqrstuvwxyz"
alp = "abcdefghijklmnopqrstuvwxyz"

for _ in range(q):
    a, b = map(str, input().split())
    alp = alp.replace(a, b)

print(s.translate(str.maketrans(all,alp)))


