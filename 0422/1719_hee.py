from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijk():
    ans = [['-'] * n for _ in range(n)]
    D = [[INF] * (n+1) for _ in range(n+1)] # 각 노드를 시작점으로 했을 때 확인해야하므로 소요 시간이 담길 2차원 배열

    for i in range(1, n+1):
        ST = []
        for t, n2 in G[i]:
            D[i][n2] = t
            ans[i-1][n2-1] = n2
            ST.append((t, n2, n2)) # 현재 노드까지 소요 시간, 현재 노드, 현재 노드이기 위해 가장 먼저 거쳐야 하는 노드

        while ST:
            t, n1, next = heappop(ST)
            if t > D[i][n1]:
                continue
            for cost, n2 in G[n1]:
                if n2 != i and t + cost < D[i][n2]: # 시작 노드는 제외
                    D[i][n2] = t + cost
                    ans[i-1][n2-1] = next # 거리가 갱신되는 경우 거쳐야 하는 노드도 갱신
                    heappush(ST, (D[i][n2], n2, next))

    for i in ans:
        print(*i)

n, m = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    n1, n2, t = map(int, input().split())
    G[n1].append((t, n2))
    G[n2].append((t, n1))
dijk()