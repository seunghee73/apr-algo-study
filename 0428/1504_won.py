import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def f(start):
    qu = []
    distArr = [INF] * (N + 1)
    qu.append((0, start))
    distArr[start] = 0
    while qu:
        curDist, curNode = heappop(qu)

        if distArr[curNode] < curDist:
            continue

        for newDist, newNode in G[curNode]:
            if distArr[newNode] > curDist + newDist:
                distArr[newNode] = curDist + newDist
                heappush(qu, (curDist + newDist, newNode))
    return distArr

INF = 8000001
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

v1, v2 = map(int, input().split())

arr1 = f(1)
arrV1 = f(v1)
arrV2 = f(v2)
ans = min(arr1[v1] + arrV1[v2] + arrV2[N], arr1[v2] + arrV2[v1] + arrV1[N])
if ans >= INF:
    ans = -1
print(ans)
