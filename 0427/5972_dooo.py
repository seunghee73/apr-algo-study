import heapq
def dijk(start):
    global total
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if now not in lst:
            lst.append(now)
        for j in G[now]:
            cost = d[now] + j[1]
            if d[j[0]] > cost:
                d[j[0]] = cost
                total[j[0]] = j[1]

                heapq.heappush(q, (cost, j[0]))

n, m = map(int, input().split())
inf = 1e9
d = [inf] * (n+1)
G = [[] for _ in range(n+1)]
total = [0] * (n+1)
lst = []
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
dijk(1)
print(d[n])