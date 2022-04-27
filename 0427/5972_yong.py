# 다익스트라 복습문제, 힙큐로 풀기

import heapq
import sys
input = sys.stdin.readline
def dijk():
    D = [1000000000] * (N+1)
    D[1] = 0
    q = []
    heapq.heappush(q, (1, 0))
    while q:
        start, food = heapq.heappop(q)
        if D[start] < food:
            continue
        else:
            for e, f in G[start]:
                if D[e] > food + f:
                    D[e] = food + f
                    heapq.heappush(q, (e, food+f))
    return D[N]

N, M = map(int,input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    s, e, f = map(int, input().split())
    G[s].append((e, f))
    G[e].append((s, f))
print(dijk())