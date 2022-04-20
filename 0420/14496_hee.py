from collections import deque, defaultdict
import sys
input = sys.stdin.readline
INF = 10 ** 9

a, b = map(int, input().split())
N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

V = [INF] * (N+1)
V[a] = 0
ST = deque([a])

while ST:
    s = ST.popleft()
    if s == b:
        print(V[s])
        break
    for i in G[s]:
        if V[s]+1 < V[i]:
            V[i] = V[s] + 1
            ST.append(i)
else:
    print(-1)