import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    Q = [(0, 0, 0)]
    visit = set()

    while Q:
        cost, curR, curC = heappop(Q)
        if (curR, curC) in visit: continue
        if (curR, curC) == (N - 1, N - 1): return cost
        visit.add((curR, curC))

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < N and 0 <= newC < N and (newR, newC) not in visit:
                heappush(Q, (cost + (rooms[newR][newC] + 1) % 2, newR, newC))

    return 0


N = int(input().rstrip())
rooms = [list(map(int, input().rstrip())) for _ in range(N)]

print(dijkstra())

