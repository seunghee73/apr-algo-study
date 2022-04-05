n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        dps = 0
        if 0<=i<n:
            dp[i+1][j] += dp[i][j]
        if 0<=j<m:
            dp[i][j+1] += dp[i][j]
        if 0<=i<n and 0<=j<m:
            dp[i+1][j+1] += dp[i][j]
print(dp[-1][-1]%1000000007)