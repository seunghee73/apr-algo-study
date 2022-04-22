import heapq
import collections
import sys

inf = sys.maxsize
input = sys.stdin.readline

graph = collections.defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

ans = [[0]*n for _ in range(n)]
def dijkstra():
    for i in range(1, n+1):
        time = [inf] * (n+1)
        path = ['-' for _ in range(n+1)]
        q = [(0, i)]
        time[i] = 0
        while q:
            t, node = heapq.heappop(q)
            if time[node] < t:
                continue
            for v, w in graph[node]:
                if t+w < time[v]:
                    time[v] = t+w
                    heapq.heappush(q, (t+w, v))
                    path[v] = node

        for j in range(1, n+1):
            ans[j-1][i-1] = path[j]
    return

dijkstra()
for a in ans:
    print(*a)
