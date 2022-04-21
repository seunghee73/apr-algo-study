import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def f():
    qu = []
    visited = [0] * N
    qu.append((0, 0))
    while qu:
        time, node = heappop(qu)
        if node == N - 1:
            return time
        if visited[node] == 1:
            continue
        visited[node] = 1
        for t, v in graph[node]:
            if visited[v] == 0:
                heappush(qu, (t + time, v))
    return -1

N, M = map(int, input().split())
ARR = list(map(int, input().split()))
ARR[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    if ARR[u] == 0 and ARR[v] == 0:
        graph[u].append((w, v))
        graph[v].append((w, u))

ans = f()
print(ans)
