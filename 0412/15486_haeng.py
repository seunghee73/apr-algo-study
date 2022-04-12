N= int(input())
Nlist=[]
for _ in range(N):
    Nlist.append(list(map(int, input().split())))

dp = [0] * (N+1)
money = 0
for i in range(N):
    if dp[i] > money:
        money = dp[i]

    if i + Nlist[i][0] > N:
        continue

    dp[i+Nlist[i][0]] = max(Nlist[i][1]+money, dp[i+Nlist[i][0]])

print(max(dp))
