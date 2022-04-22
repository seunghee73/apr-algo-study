import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def f(s):
    path = ['-'] * (N + 1)
    qu = [(0, s)]
    timeArr[s] = 0
    while qu:
        curTime, curNode = heappop(qu)

        if timeArr[curNode] < curTime:
            continue
        for newTime, newNode in graph[curNode]:
            if timeArr[newNode] > curTime + newTime:
                timeArr[newNode] = curTime + newTime
                heappush(qu, (curTime + newTime, newNode))
                path[newNode] = curNode
    return path[1:]

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

ans = [[0] * (N) for _ in range(N)]
for i in range(N):
    timeArr = [200001] * (N + 1)
    path = f(i + 1)
    for k in range(N):
        ans[k][i] = path[k]

for i in ans:
    print(*i)
