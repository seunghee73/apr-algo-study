from collections import defaultdict
from heapq import *
N = int(input())
M = int(input())
G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
S, E = map(int, input().split())

INF = 10 ** 9
V = [INF] * (N+1)
V[S] = 0
ST = [(0, S)]
while ST:
    c, n1 = heappop(ST)
    if c > V[n1]:
        continue
    for cost, n2 in G[n1]:
        if V[n1] + cost < V[n2]:
            V[n2] = V[n1] + cost
            ST.append((cost, n2))
print(V[E])
