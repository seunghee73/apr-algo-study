import heapq
def dijk(start, end):
    d = [inf] * (n + 1)
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return d[end]

        for j in G[now]:
            cost = d[now] + j[1]
            if cost < d[j[0]]:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
def ans(v1, v2):
    s = dijk(1, v1)
    p = dijk(v1, v2)
    e = dijk(v2, n)
    if s == None or p == None or e == None:
        return -1
    else:
        return s + p +e
n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
v1, v2 = map(int, input().split())
inf = 1e9

ans1 = ans(v1, v2)
ans2 = ans(v2, v1)
if ans1 < ans2:
    print(ans1)
else:
    print(ans2)
