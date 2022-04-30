import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def f(s):
    cnt = 0
    qu = []
    qu.append((0, s))
    timeArr[s] = 0
    while qu:
        curTime, curNode = heappop(qu)
        if visited[curNode] == 0:
            visited[curNode] = 1
            cnt += 1

        if timeArr[curNode] < curTime:
            continue

        for newTime, newNode in G[curNode]:
            if timeArr[newNode] > curTime + newTime:
                timeArr[newNode] = curTime + newTime
                heappush(qu, (curTime + newTime, newNode))
    return cnt

T = int(input())

for _ in range(1, T + 1):
    n, d, c = map(int, input().split())
    G = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append((s, a))
    cnt = 0
    ans = 0
    timeArr = [10000001] * (n + 1)
    visited = [0] * (n + 1)
    cnt = f(c)
    for i in timeArr:
        if ans < i and i != 10000001:
            ans = i
    print('{} {}'.format(cnt, ans))
