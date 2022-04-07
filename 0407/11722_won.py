N = int(input())
ARR = list(map(int, input().split()))
dp = [0] * N
cnt = [0] * N

for r in range(N):
    idx = 0
    maxV = 0
    maxC = 0
    flag = False
    for c in range(0, r):
        if ARR[r] < ARR[c] and maxC < cnt[c]:
            maxC = cnt[c]
            idx = c
            flag = True
    if flag:
        dp[r] = dp[idx] + ARR[r]
        cnt[r] = cnt[idx] + 1
    else:
        dp[r] = ARR[r]
        cnt[r] = 1
# print(ARR)
# print(dp)
# print(cnt)
print(max(cnt))
