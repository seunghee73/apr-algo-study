N, M = map(int, input().split())
DP = [[0] * M for _ in range(N)]
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

ans = 0
for y in range(N):
    for x in range(M):
        if -1 < x-1 < M:
            DP[y][x] = DP[y][x-1]
        if -1 < y-1 < N:
            DP[y][x] = max(DP[y][x], DP[y-1][x])
        DP[y][x] += G[y][x]
        ans = max(ans, DP[y][x])
print(ans)
