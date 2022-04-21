import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra():
    Q = [(0, 0)]  # cost, 현재 위치

    while Q:
        curCost, curV = heappop(Q)
        if visited[curV]: continue
        visited[curV] = 1
        if curV == N - 1: return curCost

        for nexCost, nexV in adj[curV]:
            if not visited[nexV]:
                heappush(Q, (curCost + nexCost, nexV))

    return -1



N, M = map(int, input().split())
visited = list(map(int, input().split()))
visited[-1] = 0

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj[a].append((t, b))
    adj[b].append((t, a))

print(dijkstra())