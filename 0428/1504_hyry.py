
import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def dijkstra(start, end):
    Q = [(0, start)]
    visit = set()

    while Q:
        curCost, curV = heappop(Q)
        if curV in visit: continue
        if curV == end: return curCost
        visit.add(curV)

        for neiCost, neiV in adj[curV]:
            if neiV not in visit:
                heappush(Q, (curCost + neiCost, neiV))

    return -1


N, E = map(int, input().rstrip().split())

adj = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

v1, v2 = map(int, input().rstrip().split())

ans1, ans2, ans3 = dijkstra(1, v1), dijkstra(v1, v2), dijkstra(v2, N)
res1, res2, res3 = dijkstra(1, v2), ans2, dijkstra(v1, N)


if 1 == v1: ans1 = 0
if v2 == N: ans3 = 0

if ans1 >= 0 and ans2 >= 0 and ans3 >= 0:
    case1 = ans1 + ans2 + ans3
else: case1 = -1

if res1 >= 0 and res2 >= 0 and res3 >= 0:
    case2 = res1 + res2 + res3
else: case2 = -1

if case1 != -1:
    if case2 != -1:
        print(min(case1, case2))
    else:
        print(case1)
else:
    if case2 != -1:
        print(case2)
    else:
        print(-1)



'''

4 2
1 2 10
2 3 5
2 3

#-1

8 8
1 2 4
1 7 6
2 8 1
2 4 2
3 8 3
4 5 4
5 7 3
7 8 5
2 7

#13

6 5
1 2 1
2 3 1
3 4 1
3 5 1
3 6 1
4 5

#7


6 4
1 2 1
2 3 2
3 4 3
5 6 4
4 5

#-1

5 5
1 2 1
1 3 1
2 3 1
3 4 1
2 5 1
3 4

#5

2 0
1 2

#-1

2 1
1 2 1
1 2

#1

3 2
1 2 1
2 3 1
1 3

#2
'''