import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = []
    v[sx][sy] = 1
    heapq.heappush(q, (0, 0, 0))
    while q:
        c, cx, cy = heapq.heappop(q)
        if cx == n-1 and cy == n-1:
            print(c)
            return
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx <n and 0 <= ny <n and v[nx][ny] == 0:
                v[nx][ny] = 1
                if arr[nx][ny] == 0:
                    heapq.heappush(q, (c+1, nx, ny))
                else:
                    heapq.heappush(q, (c, nx, ny))

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
v = [[0] * n for _ in range(n)]

bfs(0, 0)
