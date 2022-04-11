N = int(input())

dp = [0] * 91
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5

for i in range(6, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N])
