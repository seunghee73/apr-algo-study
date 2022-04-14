
N = int(input())
memo = [0] * 1_000_001
memo[1] = 1
div = 1_000_000_000

newN = abs(N)
for i in range(2, newN + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % div
    memo[i] %= div

if N > 0:
    print(1)
    print(memo[N])
elif N == 0:
    print(0)
    print(0)
else:
    if newN % 2 == 0:
        print(-1)
        print(memo[newN])
    else:
        print(1)
        print(memo[newN])