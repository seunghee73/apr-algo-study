from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    D = [INF] * (N+1)
    D[1] = 0
    Q = [(0, 1)]
    while Q:
        c, n1 = heappop(Q)
        if D[n1] < c:
            continue

        for cost, n2 in G[n1]:
            if cost + D[n1] < D[n2]:
                D[n2] = cost + D[n1]
                heappush(Q, (D[n2], n2))
    return D

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))
print(dijkstra()[-1])

