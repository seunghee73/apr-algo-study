import heapq
import collections
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
for i in range(d+1):
    graph[i].append((i+1, 1))

dist = [1e9]*(d+1)
def dijkstra():
    q = [(0, 0)]
    dist[0] = 0
    while q:
        t, node = heapq.heappop(q)
        if dist[node] < t:
            continue
        for v, w in graph[node]:
            if v<=d and  t+w < dist[v]:
                dist[v] = t+w
                heapq.heappush(q, (t+w, v))
    print(dist[-1])
    return

dijkstra()
