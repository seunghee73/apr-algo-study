import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(S):
    global t, cnt
    Q = [(0, S)]
    visit = set()

    while Q and len(visit) < N:
        cost, curV = heappop(Q)
        if curV in visit: continue

        visit.add(curV)
        cnt += 1
        t = max(t, cost)

        if len(visit) == N: return

        for neiCost, neiV in edges[curV]:
            if neiV not in visit:
                heappush(Q, (cost + neiCost, neiV))


T = int(input())
for _ in range(T):
    N, E, S = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges[b].append((w, a))
    t = cnt = 0
    dijkstra(S)
    print(cnt, t)