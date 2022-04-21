import heapq
import collections
import sys

inf = sys.maxsize
input = sys.stdin.readline

graph = collections.defaultdict(list)
n, m = map(int, input().split())
detect = list(map(int, input().split()))
detect[-1] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [inf] * (n)
def dijkstra():
    if detect[0] == 1:
        return
    q = [(0, 0)]
    dist[0] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v] and detect[v] == 0:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))
    print(dist[-1]) if dist[-1] != inf else print(-1)
    return

dijkstra()
