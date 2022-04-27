# n개의 노드, m개의 간선/ 양방향/ 간선마다 c의 비용/ 두개 노드간 중복 간선 가능
# 1 -> N으로 이동
import heapq
import sys
input = sys.stdin.readline
def djk():
    global start_point, end_point, nodes, visited
    queue = []
    heapq.heappush(queue,[0,start_point])

    while queue:
        cost , now = heapq.heappop(queue)
        for node in nodes[now]:
            nxt, nxtCost = node
            if visited[nxt] > cost + nxtCost:
                visited[nxt] = cost + nxtCost
                heapq.heappush(queue,[visited[nxt],nxt])

n, m = map(int,input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int,input().split())
    nodes[s].append([e,w])
    nodes[e].append([s,w])
start_point = 1
end_point = n
visited = [float('inf') for _ in range(n+1)]
visited[start_point] = 0
djk()
print(visited[end_point])