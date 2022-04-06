n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    maxV = 0
    idx = 0
    flag = 0
    for j in range(0, i):
        if arr[i] > arr[j] and maxV < dp[j]:
            idx = j
            maxV = dp[j]
            flag = 1
    if flag:
        dp[i] = arr[i] + dp[idx]
    else:
        dp[i] = arr[i]
# print(dp)
print(max(dp))
