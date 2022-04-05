n, m = map(int, input().split())
DP = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            DP[i][j] = 1
        else:
            DP[i][j] = (DP[i][j-1] + DP[i-1][j] + DP[i-1][j-1]) % 1_000_000_007
print(DP[-1][-1])