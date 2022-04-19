
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


N = int(input())
M = int(input())

adj = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    S, E, W = map(int, input().split())
    adj[S].append((E, W))
A, B = map(int, input().split())

Q = [(0, A)]  
visited = [False] * (N + 1)
cost = 0 

while Q:
    curW, curV = heappop(Q)
    if visited[curV]: continue

    if curV == B:
        cost = curW
    visited[curV] = True

    for nexV, nexW in adj[curV]:
        if not visited[nexV]:
            heappush(Q, (curW + nexW, nexV))

print(cost)