import heapq
import collections
import sys

input = sys.stdin.readline
graph = collections.defaultdict(list)
n = int(input())
m = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
x, y = map(int, input().split())

cost = [1e9]*(n+1)
ans = []
def dijkstra():
    q = [(0, x)]
    cost[x] = 0
    while q:
        c, node = heapq.heappop(q)
        if cost[node] < c:
            continue
        for v, w in graph[node]:
            if c+w < cost[v]:
                cost[v] = c+w
                heapq.heappush(q, (c+w, v))

    print(cost[y])
    return

dijkstra()