N = int(input())
seiza = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
sky = [list(map(int, input().split())) for _ in range(M)]

first = seiza[0]
for star in sky:
    x = star[0] - first[0]
    y = star[1] - first[1]
    check = True
    #print(f"x = {x}, y = {y}")
    for seiza_stars in seiza:
        x_check = seiza_stars[0] + x
        y_check = seiza_stars[1] + y
        if [x_check, y_check] in sky:
            #print("ok")
            continue
        else:
            check = False
            break
    if check:
        print(x, y)
        exit()
