import sys
from collections import deque
input = sys.stdin.readline


def bfs(row, col):
    global maxV
    Q = deque()
    visited = [[False] * cols for _ in range(rows)]

    route = 0
    Q.append(((row, col), route))
    visited[row][col] = True

    while Q:
        (curR, curC), route = Q.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < rows and 0 <= newC < cols and MAP[newR][newC] == 'L'\
                    and not visited[newR][newC]:
                Q.append(((newR, newC), route + 1))
                visited[newR][newC] = True
                if maxV < route + 1:
                    maxV = route + 1


rows, cols = map(int, input().rstrip().split())  # 세로, 가로
MAP = [list(input().rstrip()) for _ in range(rows)]

maxV = -1
for r in range(rows):
    for c in range(cols):
        if MAP[r][c] == 'L':
            bfs(r, c)

print(maxV)