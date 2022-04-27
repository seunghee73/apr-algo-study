import heapq
import collections
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [1e9]*(n+1)

def dijkstra():
    q = [(0, 1)]
    dist[1] = 0
    while q:
        c, node = heapq.heappop(q)
        if dist[node] < c:
            continue
        for v, w in graph[node]:
            if c+w < dist[v]:
                dist[v] = c+w
                heapq.heappush(q, (c+w, v))
    print(dist[-1])
    return

dijkstra()