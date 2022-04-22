# 미완성

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def f(s, e):
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

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

timeArr = [200001] * (N + 1)
ans = f(1, 6)
print(timeArr)
# ans = [[0] * N for _ in range(N)]
# for i in range(N):
#     for k in range(N):
#         if i == k:
#             ans[i][k] = '-'
#             continue
#         result = f(i + 1, k + 1)
#         ans[i][k] = result
