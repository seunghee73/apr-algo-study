
import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

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

n = int(input())
m = int(input())
G = [[] for _ in range(n+1)]
v = [0] * (n+1)
d = [inf] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
s, e = map(int, input().split())
dijkstra(s)
print(d[e])


