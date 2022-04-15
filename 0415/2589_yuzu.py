from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

search = deque()
s = 0
while not search:
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'L':
                f = 0
                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 'L':
                        f += 1
                if s+1 == f:
                    search.append([i, j])
    s += 1

max = 0
for sea in search:
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([sea[0], sea[1], 0])
    visited[sea[0]][sea[1]] = 1
    while q:
        x, y, cnt = q.popleft()
        if cnt > max:
            max = cnt
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny, cnt+1])
print(max)