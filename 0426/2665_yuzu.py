import heapq

n = int(input())
arr = [list(input()) for _ in range(n)]

def bfs():
    q = [(0, 0, 0)]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        b, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            return b
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if arr[nx][ny] == '1':
                    heapq.heappush(q, (b, nx, ny))
                    visited[nx][ny] = 1
                elif arr[nx][ny] == '0':
                    heapq.heappush(q, (b+1, nx, ny))
                    visited[nx][ny] = 1

print(bfs())