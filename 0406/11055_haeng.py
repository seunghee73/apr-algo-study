N=int(input())
Nlist=list(map(int,input().split()))
dp = [0] * N
dp[0] = Nlist[0]
for i in range(1,N):
    m = 0
    for j in range(0,i):
        if Nlist[i] > Nlist[j] and m < dp[j]:
            m = dp[j]

    dp[i] = m + Nlist[i]

print(max(dp))


