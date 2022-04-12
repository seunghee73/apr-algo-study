N = int(input())
dp = [0] * (N + 2)
t = [0] * (N + 1)
p = [0] * (N + 1)
for i in range(1, N + 1):
    a, b = map(int, input().split())
    t[i] = a
    p[i] = b
for i in range(1, N + 1):
    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]
    if i + t[i] <= N + 1 and dp[i + t[i]] < dp[i] + p[i]:
        dp[i + t[i]] = dp[i] + p[i]

print(max(dp))
