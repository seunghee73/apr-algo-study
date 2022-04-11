def pinary(n):
    k = 2
    while k <= n:
        dp[k] = dp[k-1]+dp[k-2]
        k += 1

dp = [0, 1] + [0]*89
n = int(input())
pinary(n)
print(dp[n])