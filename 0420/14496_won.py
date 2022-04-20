import sys
input = sys.stdin.readline
from collections import deque

def f(s):
    qu = deque()
    visited = [0] * (N + 1)
    qu.append(s)
    visited[s] = 1
    while qu:
        t = qu.popleft()

        if t == b:
            return visited[t] - 1

        for v in graph[t]:
            if not visited[v]:
                qu.append(v)
                visited[v] = visited[t] + 1
    return -1

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
ans = f(a)
print(ans)
