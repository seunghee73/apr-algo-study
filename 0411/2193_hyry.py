
def pinary(N):
    if N > 1 and not memo[N]:
        memo[N] = pinary(N - 1) + pinary(N - 2)
    return memo[N]


N = int(input())
memo = [0] * (N + 1)
memo[0], memo[1] = 0, 1
print(pinary(N))
