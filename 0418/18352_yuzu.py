import heapq
import collections
import sys

input = sys.stdin.readline
graph = collections.defaultdict(list)
n, m, k, x = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append((v, 1))
dist = [1e9]*(n+1)
ans = []

def dijkstra():
    q = [(0, x)]
    dist[x] = 0
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for v, w in graph[node]:
            if d+w < dist[v]:
                dist[v] = d+w
                heapq.heappush(q, (d+w, v))

    for i in range(1, n+1):
        if dist[i] == k:
            ans.append(i)

dijkstra()
print(-1) if len(ans)==0 else print(*ans, sep='\n')