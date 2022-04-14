N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4, abs(N) + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000000

if N < 0 and N % 2 == 0:
    print(-1)
elif N == 0:
    print(0)
else:
    print(1)
print(dp[abs(N)])