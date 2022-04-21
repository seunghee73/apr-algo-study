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
G = [[] for _ in range(n)]
v = [0] * (n)
d = [inf] * (n)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a != n - 1 and b != n - 1 and (lst[a] == 1 or lst[b] == 1):
        continue
    G[a].append((b, c))
    G[b].append((a, c))
dijkstra(0)
if d[n-1] == inf:
    print(-1)
else:
    print(d[n-1])