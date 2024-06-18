import math
w, h, b = map(int, input().split())

goal = b * h * h / 10000
print(0) if goal >= w else print(math.ceil(w - goal)) 