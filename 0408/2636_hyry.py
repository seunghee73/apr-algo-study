
import sys
input = sys.stdin.readline


def melting(row, col):
    D = ((1, 0), (-1, 0), (0, 1), (0, -1))
    Q = [(row, col)]
    visited = [[False] * C for _ in range(R)]
    visited[row][col] = True
    melted = set()

    while Q:
        curR, curC = Q.pop(0)
        for dr, dc in D:
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C and not visited[newR][newC] and\
                not board[newR][newC]:
                Q.append((newR, newC))
                visited[newR][newC] = True
                for dr2, dc2 in D:
                    nxtR, nxtC = newR + dr2, newC + dc2
                    if 0 <= nxtR < R and 0 <= nxtC < C and board[nxtR][nxtC]:
                        melted.add((nxtR, nxtC))

    return melted


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

rest = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            rest += 1

mel = melting(0, 0)
tm = 1 if rest else 0

while mel and rest - len(mel) > 0:

    for (i, j) in mel:
        board[i][j] = 0
        rest -= 1
    mel = melting(0, 0)
    tm += 1

print(tm)
print(rest)