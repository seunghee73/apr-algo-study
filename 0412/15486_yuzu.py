import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    t, p = map(int, input().split())
    a.append((t, p))

dp = [0]*(n+1)
for i in range(n):
    if i + a[i][0] < n+1:
        dp[i+a[i][0]] = max(dp[i+a[i][0]], dp[i]+a[i][1])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[-1])