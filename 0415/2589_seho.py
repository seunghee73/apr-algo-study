from collections import deque
import sys
input = sys.stdin.readline
def bfs(loc):
    global answer, n, m, board
    visited = [[0]*m for _ in range(n)]
    queue = deque([[loc[0],loc[1]]])
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    visited[loc[0]][loc[1]] = 1
    while queue:
        tmp = queue.popleft()

        for move in moves:
            row = tmp[0] + move[0]
            col = tmp[1] + move[1]
            if 0 <= row < n and 0 <= col < m and board[row][col] == "L" and visited[row][col] == 0:
                visited[row][col] = visited[tmp[0]][tmp[1]] + 1
                if answer < visited[row][col]:
                    answer = visited[row][col]
                queue.append([row,col])

n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]

answer = 0

for row in range(n):
    for col in range(m):
        if board[row][col] == "L":
            bfs([row,col])

print(max(0,answer-1))
## python으로는 불통, pypy는 통과..