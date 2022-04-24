import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize
def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    d = [100000000 for i in range(n + 1)]
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in G[now]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
                arr[i[0] - 1][start - 1] = now
n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
arr = [[0] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
for i in range(1, n + 1):
    dijkstra(i)
for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()