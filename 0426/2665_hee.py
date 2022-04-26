import sys, heapq
n = int(input())
M = []
INF = sys.maxsize

for _ in range(n):
    M.append(list(input()))

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
Q = [(0, 0, 0)]
V = [[INF] * n for _ in range(n)]
V[0][0] = 0

ans = INF
while Q:
    c, x, y = heapq.heappop(Q)

    if x == y == n-1 :
        ans = min(ans, c)
        continue

    if ans < c or V[y][x] < c :
        continue

    for d in D:
        nx = x + d[0]
        ny = y + d[1]
        if -1 < nx < n and -1 < ny < n:
            if M[ny][nx] == '0' and c+1 < V[ny][nx]:
                heapq.heappush(Q, (c+1, nx, ny))
                V[ny][nx] = c+1
            elif M[ny][nx] == '1' and c < V[ny][nx]:
                heapq.heappush(Q, (c, nx, ny))
                V[ny][nx] = c
print(ans)