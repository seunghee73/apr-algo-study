import heapq
import collections
import sys

INF = sys.maxsize
input = sys.stdin.readline

def dijkstra():
    depend = [INF] * (n+1)
    q = [(0, c)]
    depend[c] = 0
    while q:
        d, node = heapq.heappop(q)
        if depend[node] < d:
            continue
        for u, w in graph[node]:
            if d+w < depend[u]:
                depend[u] = d+w
                heapq.heappush(q, (d+w, u))
    return depend

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(d):
        u, v, w = map(int, input().split())
        graph[v].append((u, w))

    depend = dijkstra()
    cnt = 0
    max = 0
    for de in depend:
        if de != INF:
            cnt += 1
            if max < de:
                max = de
    print(cnt, max)