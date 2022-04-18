dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    global max_val
    q = []
    q.append((sx, sy))
    v = [[0] * m for _ in range(n)]
    v[sx][sy] = 1
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and v[nx][ny] == 0 and arr[nx][ny] == 'L':
                v[nx][ny] = v[cx][cy] + 1
                q.append((nx, ny))
    if v[cx][cy] > max_val:
        max_val = v[cx][cy]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
max_val = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            bfs(i, j)
print(max_val-1)
