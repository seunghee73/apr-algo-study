import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# 가장 바깥 visited 처리
qu = deque()
visited = [[0] * M for _ in range(N)]
qu.append((0, 0))
visited[0][0] = 1
while qu:
    cr, cc = qu.popleft()
    for dr, dc in[[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = cr + dr
        nc = cc + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and MAP[nr][nc] == 0:
            qu.append((nr, nc))
            visited[nr][nc] = 1

# 치즈 구멍 2로 맵핑
def chHole(sr, sc):
    qu = deque()
    qu.append((sr, sc))
    visited[sr][sc] = 1
    MAP[sr][sc] = 2
    while qu:
        cr, cc = qu.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and MAP[nr][nc] == 0:
                qu.append((nr, nc))
                visited[nr][nc] = 1
                MAP[nr][nc] = 2

# 치즈 구멍 = 2로 맵핑
for i in range(N):
    for k in range(M):
        if MAP[i][k] == 0 and not visited[i][k]:
            chHole(i, k)

# 공기와 맞닿아 있으면 True, 아니면 False
def touchOutside(r, c):
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and MAP[nr][nc] == 0:
            return True
    return False

# 구멍이 공기와 닿아 있으면 0 처리
def hole(sr, sc):
    qu = deque()
    visited = [[0] * M for _ in range(N)]
    qu.append((sr, sc))
    visited[sr][sc] = 1
    while qu:
        cr, cc = qu.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and MAP[nr][nc] == 2:
                qu.append((nr, nc))
                visited[nr][nc] = 1
                MAP[nr][nc] = 0

sol = []
while True:
    cnt = 0
    # 없앨 겉 치즈 담기
    tmp = []
    for i in range(N):
        for k in range(M):
            # 치즈 겉
            if MAP[i][k] == 1 and touchOutside(i, k):
                cnt += 1
                tmp.append((i, k))
    # 0이면 치즈 없음
    if cnt == 0:
        break
    sol.append(cnt)

    # 겉 치즈 제거
    for i, k in tmp:
        MAP[i][k] = 0

    # 구멍이 공기와 닿으면 주변 구멍도 싹 공기로
    for i in range(N):
        for k in range(M):
            if MAP[i][k] == 2 and touchOutside(i, k):
                hole(i, k)
# print(sol)
print(len(sol))
print(sol[-1])
