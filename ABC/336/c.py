def to_base_5(n):
    if n == 0:
        return '0'
    
    base_5 = []
    while n > 0:
        base_5.append(str((n % 5)*2))
        n //= 5
    
    return ''.join(reversed(base_5))

n = int(input())
n -= 1
print(to_base_5(n))