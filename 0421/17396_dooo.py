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
lst = list(map(int, input().split()))
G = [[] for _ in range(n+1)]
v = [0] * (n+1)
d = [inf] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())

    G[a].append((b, c))
    G[b].append((a, c))
print(1)
dijkstra(1)

if d[n-1] == inf:
    print(-1)
else:
    print(d[n-1])