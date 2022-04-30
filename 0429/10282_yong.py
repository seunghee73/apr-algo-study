# 평범한 다익스트라문제
# 감염된 컴퓨터 수를 카운팅하기 위해 새로운 리스트를 만들었지만 다른 방법이 있을까?
import heapq
import sys
input = sys.stdin.readline

def dijk():
    D = [1000000000000] * (n+1)
    D[c] = 0
    q = []
    heapq.heappush(q, (c, 0))
    while q:
        now, dis = heapq.heappop(q)
        if D[now] < dis:
            continue
        for a, s in G[now]:
            if D[a] > dis + s:
                D[a] = dis + s
                ans[a] = dis+s
                heapq.heappush(q, (a, dis+s))

T = int(input())
for tc in range(1, T+1):
    n, d, c = map(int, input().split())
    ans = [-1] * (n+1)
    ans[c] = 0
    G = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        G[b].append((a, s))
    dijk()
    print(len(ans) - ans.count(-1), end=' ')
    print(max(ans))