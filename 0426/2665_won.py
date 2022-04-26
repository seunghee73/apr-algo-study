import sys
input = sys.stdin.readline
# from collections import deque
from heapq import heappush, heappop

def f():
    qu = []
    visited = [[0] * N for _ in range(N)]
    qu.append((0, 0, 0))
    visited[0][0] = 1
    while qu:
        cnt, curR, curC = heappop(qu)

        if curR == N - 1 and curC == N - 1:
            return cnt

        for dc, dr in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            newR = curR + dr
            newC = curC + dc
            if 0 <= newR < N and 0 <= newC < N and visited[newR][newC] == 0:
                visited[newR][newC] = 1
                if G[newR][newC] == 1:
                    heappush(qu, (cnt, newR, newC))
                else:
                    heappush(qu, (cnt + 1, newR, newC))

N = int(input())
G = [list(map(int, input().rstrip())) for _ in range(N)]

ans = f()
print(ans)
