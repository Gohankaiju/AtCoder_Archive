import sys
from collections import defaultdict
def step1():
    input_file_path = "/home/gohankaiju/AtCoder/ABC/dena/input.txt"
    with open(input_file_path, 'r') as file:
        input_data = file.read()
    #input_data = sys.stdin.read()
    lines = input_data.splitlines()

    step = lines[0]
    M = int(lines[1])
    Menu = defaultdict(int)

    for line in lines[2:M+2]:
        d, s, p = map(int, line.split())
        Menu[d] = [s, p]

    for line in lines[M+2:]:
        od, t, d, n = map(str, line.split())
        d = int(d)
        n = int(n)

        if Menu[d][0] -n < 0:
            print(f"sold out {t}")
        else:
            Menu[d][0] -= n
            for _ in range(n):    
                print(f"received order {t} {d}")

def step2():
    input_file_path = "/home/gohankaiju/AtCoder/ABC/dena/input.txt"
    with open(input_file_path, 'r') as file:
        input_data = file.read()
    # input_data = sys.stdin.read()
    lines = input_data.splitlines()

    step = lines[0]
    waiting = []
    cook = []
    M, K = map(int, lines[1].split())
    Menu = defaultdict(int)

    for line in lines[2:M+2]:
        d, s, p = map(int, line.split())
        Menu[d] = [s, p]

    for line in lines[M+2:]:
        od = list(line.split())
        if od[0] == "received":
            if Menu[d][0] -1 < 0:
                Menu[d][0] -= 1
                print(f"sold out {od[3]}")
            else:
                if K - 1 < 0:
                    waiting.append(od[3])
                    print("wait")
                else:
                    K -= 1
                    cook.append(od[3])
                    print(od[3])
        elif od[0] == "complete":
            if od[1] in cook:
                if(len(waiting) != 0):
                    print(f"ok {waiting[0]}")
                    cook.append(waiting[0])
                    waiting.pop(0)
                else:
                    print("ok")
            else:
                print("unexpected input")

                
def main():
    step2()

if __name__ == "__main__":
    main()