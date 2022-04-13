N,M = map(int,input().split())
Nlist=[]
for _ in range(N):
    Nlist.append(list(map(int,input().split())))

dp = [[0]*M for _ in range(N)]
dp[0][0] = Nlist[0][0]

for y in range(N):
    for x in range(M):
        if x == 0 and y > 0:
            dp[y][x] = dp[y-1][x] + Nlist[y][x]

        elif y == 0 and x > 0:
            dp[y][x] = dp[y][x-1] + Nlist[y][x]

        elif y>0 and x>0:
            dp[y][x] = max(dp[y][x-1],dp[y-1][x]) + Nlist[y][x]
print(dp[N-1][M-1])





