import sys
input = sys.stdin.readline
from collections import deque

def f(sr, sc):
    maxV = 0
    qu = deque()
    qu.append((sr, sc))
    visited[sr][sc] = 1
    while qu:
        cr, cc = qu.popleft()
        maxV = max(maxV, visited[cr][cc])

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and MAP[nr][nc] == 'L':
                qu.append((nr, nc))
                visited[nr][nc] = visited[cr][cc] + 1
    return maxV

N, M = map(int, input().split())
MAP = [list(input().rstrip()) for _ in range(N)]

ans = 0
for i in range(N):
    for k in range(M):
        if MAP[i][k] == 'L':
            visited = [[0] * M for _ in range(N)]
            result = f(i, k)
            ans = max(ans, result)
print(ans - 1)
