import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def f():
    qu = [(0, 1)]
    stoverArr[1] = 0
    while qu:
        curStover, curNode = heappop(qu)

        if curNode == N:
            return stoverArr[curNode]

        if stoverArr[curNode] < curStover:
            continue

        for newStover, newNode in G[curNode]:
            if stoverArr[newNode] > curStover + newStover:
                stoverArr[newNode] = curStover + newStover
                heappush(qu, (curStover + newStover, newNode))

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((w, v))
    G[v].append((w, u))
stoverArr = [50000000] * (N + 1)
ans = f()
print(ans)
