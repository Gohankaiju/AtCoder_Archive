MOD = 998244353

def popcount(x):
    return bin(x).count('1')

def calculate_popcount_sum(N, M):
    N_bin = bin(N)[2:] 
    L = len(N_bin)
    dp = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(2)]
    
    dp[0][0][0] = 1
    
    for i in range(L):
        for smaller in range(2):
            for pop in range(L + 1):
                limit = 1 if (smaller or N_bin[i] == '1') else 0
                for digit in range(limit + 1):
                    ni = i + 1
                    nsmaller = smaller or (digit < int(N_bin[i]))
                    npop = pop + ((M >> (L - 1 - i)) & digit)
                    if npop <= L:
                        dp[nsmaller][ni][npop] += dp[smaller][i][pop]
                        dp[nsmaller][ni][npop] %= MOD

    result = 0
    for smaller in range(2):
        for pop in range(L + 1):
            result += dp[smaller][L][pop] * pop
            result %= MOD
    
    return result

N, M = map(int, input().split())
result = calculate_popcount_sum(N, M)
print(result)
