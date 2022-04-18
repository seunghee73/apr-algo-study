import sys
input = sys.stdin.readline
from collections import deque

def f(s):
    result = []
    qu = deque()
    qu.append(s)
    visited[s] = 1
    while qu:
        t = qu.popleft()
        if visited[t] == K + 1:
            result.append(t)

        for i in MAP[t]:
            if not visited[i]:
                qu.append(i)
                visited[i] = visited[t] + 1
    return result

N, M, K, X = map(int, input().split())
MAP = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    MAP[a].append(b)

ans = f(X)
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
