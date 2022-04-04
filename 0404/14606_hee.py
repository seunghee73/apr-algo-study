N = int(input())
dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + (i-1)

print(dp[-1])

