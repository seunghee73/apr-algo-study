from collections import defaultdict
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    G = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append((s, a))

    D = [INF] * (n+1)
    D[c] = 0
    Q = [(0, c)]
    while Q:
        s, n1 = heapq.heappop(Q)

        if D[n1] < s:
            continue

        for ss, n2 in G[n1]:
            if ss + s < D[n2]:
                D[n2] = ss + s
                heapq.heappush(Q, (D[n2], n2))

    computers = time = 0
    for i in D:
        if i != INF:
            time = max(time, i)
            computers += 1
    print(computers, time)