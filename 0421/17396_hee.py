from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
INF = 10 ** 12

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append((t, b))
    G[b].append((t, a))

D = [INF] * N
D[0] = 0
ST = [(0, 0)]
flag = False # 상대 넥서스에 갈 수 있는 지 없는 지

while ST:
    t, n1 = heapq.heappop(ST)
    if t > D[n1]:
        continue
    for cost, n2 in G[n1]:
        if (not A[n2] or n2 == N-1) and t + cost < D[n2]:
            if n2 == N-1:
                flag = True
            D[n2] = t + cost
            heapq.heappush(ST, (D[n2], n2))

print(D[-1]) if flag else print(-1)

