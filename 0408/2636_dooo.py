dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    global flag
    ccnt = 0

    q = []

    q.append((sx, sy))
    v[sx][sy] = 1
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx, ny))
            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == 1:
                wall.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                ccnt += 1
    if ccnt == 0:
        flag = 1
        return
    cnt.append(ccnt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

wall = []
cnt = []
time = 0
while True:
    time += 1
    flag = 0
    v = [[0] * M for _ in range(N)]
    bfs(0, 0)
    for r, j in wall:
        arr[r][j] = 0
    if flag == 1:
        break


print(time-1)
print(cnt[-1])