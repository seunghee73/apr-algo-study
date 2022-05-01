import heapq
def dijk(s):
    q = []
    d[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)

        for j in G[now]:
            cost = dist + j[1]
            if cost < d[j[0]]:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

inf = 1e9
TC = int(input())
for _ in range(TC):
    n, m, s = map(int, input().split())
    d = [inf] * (n+1)
    G = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        G[b].append((a, c))
    dijk(s)
    cnt = 0
    max_dist = -1
    for i in d:
        if i != inf:
            cnt += 1
            if i > max_dist:
                max_dist = i
    print(cnt, end = ' ')
    print(max_dist)