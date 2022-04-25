
from heapq import heappop, heappush


def dijkstra():
    Q = [(0, 0)]
    visit = set()

    ans = 0
    while Q:
        curW, curV = heappop(Q)
        if curV in visit: continue
        ans = curW
        visit.add(curV)

        if curV == D: return ans

        for nexW, nexV in adj[curV]:
            if nexV not in visit and nexV <= D:
                heappush(Q, (curW + nexW, nexV))

    return ans


N, D = map(int, input().split())
adj = [[(1, i + 1)] for i in range(D)] + [[]]
# 바로 옆 노드 i + 1, cost 1
nodes = {0, D}
for _ in range(N):
    s, e, w = map(int, input().split())

    if e <= D:
        if e - s < w:
            adj[s].append((e - s, e))
        else:
            adj[s].append((w, e))
        for i in nodes:
            if i < s: adj[i].append((s - i, s))
            if e < i: adj[e].append((i - e, i))
        nodes.add(s)
        nodes.add(e)

print(dijkstra())



'''
1 3
1 2 2


'''