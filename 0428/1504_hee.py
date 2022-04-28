from heapq import *
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start, dest):
    D = [INF] * (N+1)
    D[start] = 0
    Q = [(0, start)]
    while Q:
        c, n1 = heappop(Q)

        if D[n1] < c:
            continue

        for cost, n2 in G[n1]:
            if cost + c < D[n2]:
                D[n2] = cost + c
                heappush(Q, (D[n2], n2))

    return D[dest]

N, E = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

v1, v2 = map(int, input().split())

ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
print(ans) if ans < INF else print(-1)
# 경로를 찾을 수 없는 ans == INF인 경우도 생기는데 (v1==1, v2==N)
# 등호 처리 잘못해서 100%에서 틀렸습니다. 발생