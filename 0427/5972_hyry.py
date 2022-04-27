
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra():
    Q = [(0, 1)]
    visit = set()

    while Q:
        cost, curV = heappop(Q)
        if curV in visit: continue
        if curV == N: return cost
        visit.add(curV)

        for neiCost, neiV in edges[curV]:
            if neiV not in visit:
                heappush(Q, (cost + neiCost, neiV))


N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((C, B))
    edges[B].append((C, A))

print(dijkstra())
