import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())

d = [inf] * (m+1)
G = [[] for _ in range(m + 1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if (b-a) < c or b > m:
        continue
    G[a].append((b, c))
for i in range(m):
    G[i].append((i+1, 1))

d[0] = 0
dijkstra(0)
print(d[-1])