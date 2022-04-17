# L인 위치마다 visited를 생성하고 bfs를 진행해 답을 찾는 방식
def bfs(c_y, c_x):
    global result
    visited = [[0] * M for _ in range(N)]
    Q = [(c_y, c_x)]
    visited[c_y][c_x] = 1
    while Q:
        y, x = Q.pop(0)
        for dy, dx in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            if 0 <= y+dy < N and 0 <= x + dx < M and not visited[y+dy][x+dx] and arr[y+dy][x+dx] == 'L':
                Q.append((y+dy, x+dx))
                visited[y+dy][x+dx] = visited[y][x] + 1

    if result < visited[y][x] - 1:
        result = visited[y][x] - 1


N, M = map(int, input().split())
arr = []
result = 0
for i in range(N):
    arr.append(list(input()))
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i, j)
print(result)