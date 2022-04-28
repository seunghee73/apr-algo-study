# 일방향, n=10000
# 감영되는 컴퓨터 수, 걸린 시간 출력
# n*n = 100,000,000
import heapq
import sys
input = sys.stdin.readline

def djk():
    global nodes, visited, n, c
    queue = []
    heapq.heappush(queue,[0,c])
    visited[c] = 0
    while queue:
        cost, now = heapq.heappop(queue)

        for node in nodes[now]:
            nxt, nxtCost = node
            if visited[nxt] > cost + nxtCost:
                visited[nxt] = cost + nxtCost
                heapq.heappush(queue,[visited[nxt],nxt])

tc_num = int(input())

for tc in range(tc_num):
    n, d, c = map(int,input().split()) # 노드개수, 간선개수, 해킹당한 노드번호
    nodes = [[] for _ in range(n+1)]
    for _ in range(d):
        s, e, w = map(int,input().split())
        nodes[e].append([s,w])
    visited = [float('inf')]*(n+1)

    djk()
    cnt = 0
    maxV = 0
    for result in visited:
        if result < float('inf'):
            cnt += 1
            if maxV < result:
                maxV = result
    print(cnt, maxV)