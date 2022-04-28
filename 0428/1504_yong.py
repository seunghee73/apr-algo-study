import heapq
import sys
input = sys.stdin.readline
# 다익스트라의 활용 문제
# 2개의 지점을 거치므로 각 지점에서 시작하는 결과를 따로 구해 도착점까지 가는 최단거리를 구하자

def dijk(start):
    D = [1000000000] * (N+1)
    D[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dis, s = heapq.heappop(q)
        if D[s] < dis:
            continue
        for e, d in G[s]:
            if D[e] > dis + d:
                D[e] = dis + d
                heapq.heappush(q, (dis+d, e))
    return D

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
    G[e].append((s, d))
v1, v2 = map(int, input().split())
D1 = dijk(1)
D2 = dijk(v1)
D3 = dijk(v2)

D_v1 = D1[v1] + D2[v2] + D3[N]
D_v2 = D1[v2] + D3[v1] + D2[N]
minV = min(D_v1, D_v2)
if minV < 1000000000:
    print(minV)
else:
    print(-1)