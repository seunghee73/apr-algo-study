N = int(input())
DP = [[0, 0] for _ in range(N)] # [i번째 자리가 0인 경우, i번째 자리가 1인 경우]

for i in range(N):
    if i == 0:
        DP[i][1] = 1
    else:
        DP[i][0] = DP[i-1][0] + DP[i-1][1]
        DP[i][1] = DP[i-1][0]

print(DP[-1][0]+DP[-1][1])
