import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline


def dijkstra(start):

    Q = []
    for nexV, nexCost in adj[start]:
        Q.append((nexCost, nexV, nexV))
    heapify(Q) 

    cnt = 0
    while cnt < N:
        cost, curV, preV = heappop(Q)
        if dist[start][curV] != '-': continue
        dist[start][curV] = preV + 1
        cnt += 1
        if cnt == N: return

        for nexV, nexCost in adj[curV]:
            if dist[start][nexV] == '-':
                heappush(Q, (cost + nexCost, nexV, preV))


N, M = map(int, input().split())
adj = [[] for _ in range(N)]  
for _ in range(M):
    v1, v2, w = map(int, input().split())
    adj[v1 - 1].append((v2 - 1, w))
    adj[v2 - 1].append((v1 - 1, w))

dist = [['-'] * N for _ in range(N)]
for i in range(N):
    dijkstra(i)
    dist[i][i] = '-'

for d in dist:
    print(*d)