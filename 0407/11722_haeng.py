N=int(input())
Nlist=list(map(int,input().split()))
dp = [0] * N
dp[0] = 1
for i in range(1,N):
    m=0
    for j in reversed(range(0,i)):
        if Nlist[i] < Nlist[j] and m < dp[j]:
            m = dp[j]
    dp[i] = m + 1

print(max(dp))


