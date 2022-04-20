import heapq
import collections
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append((v, 1))
    graph[v].append((u, 1))

dist = [1e9]*(n+1)

def dijkstra():
    q = [(0, a)]
    dist[a] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
    return

dijkstra()
print(-1) if dist[b]==1e9 else print(dist[b])