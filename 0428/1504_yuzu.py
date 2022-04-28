import heapq
import collections
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, e = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visit1 = []
visit2 = []
x, y = map(int, input().split())
visit1.append(1)
visit1.append(x)
visit1.append(y)
visit1.append(n)
visit2.append(1)
visit2.append(y)
visit2.append(x)
visit2.append(n)

def dijkstra(visit):
    ans = 0
    for i in range(3):
        dist = [inf] * (n+1)
        q = [(0, visit[i])]
        dist[visit[i]] = 0
        while q:
            d, node = heapq.heappop(q)
            if dist[node] < d:
                continue
            for v, w in graph[node]:
                if d+w < dist[v]:
                    dist[v] = d+w
                    heapq.heappush(q, (d+w, v))
        if dist[visit[i+1]] == inf:
            return -1
        ans += dist[visit[i+1]]
    return ans

a = dijkstra(visit1)
b = dijkstra(visit2)
if a != -1 and b != -1:
    print(min(a, b))
elif a != -1 or b != -1:
    print(max(a, b))
else:
    print(-1)