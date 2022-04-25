import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def f():
    qu = [(0, 0)]
    distArr[0] = 0
    while qu:
        curDist, curNode = heappop(qu)
        if distArr[curNode] < curDist:
            continue

        for newDist, newNode in G[curNode]:
            if newNode <= D and distArr[newNode] > curDist + newDist:
                distArr[newNode] = curDist + newDist
                heappush(qu, (curDist + newDist, newNode))

N, D = map(int, input().split())
G = [[] for _ in range(10001)]
for _ in range(N):
    u, v, w = map(int, input().split())
    if v - u > w:
        G[u].append((w, v))
for i in range(D + 1):
    G[i].append((1, i + 1))
distArr = [D + 1] * (D + 1)
f()
print(distArr[-1])
