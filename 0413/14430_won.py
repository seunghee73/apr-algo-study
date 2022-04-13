N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
for i in range(N):
    for k in range(M):
        if i == 0 and k > 0:
            dp[i][k] = dp[i][k - 1]
        elif i > 0 and k == 0:
            dp[i][k] = dp[i - 1][k]
        else:
            dp[i][k] = max(dp[i][k - 1], dp[i - 1][k])
        dp[i][k] += MAP[i][k]
print(dp[N - 1][M - 1])
