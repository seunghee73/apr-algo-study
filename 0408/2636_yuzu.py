from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    cheese.append(cnt)
    return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cheese = []
time = 0
while True:
    time += 1
    bfs()
    if cheese and cheese[-1] == 0:
        break

print(time-1)
print(cheese[-2])