# 양방향 그래프/ 1 -> N으로 최단거리로 이동
# 주어진 두 정점을 통과해야함.
# 사이클 가능
# 1 -> N 이동할때 주어진 두 정점을 반드시 거치는 최단경로 이동
##
import sys
import heapq
input = sys.stdin.readline

def djk(start, end):
    global nodes
    visited = [float('inf')]*(n+1)
    queue = []
    heapq.heappush(queue,[0,start])
    visited[start] = 0

    while queue:
        cost , now = heapq.heappop(queue)
        for nxt in range(1,n+1):
            if visited[nxt] > cost + nodes[now][nxt]:
                visited[nxt] = cost + nodes[now][nxt]
                heapq.heappush(queue,[visited[nxt],nxt])
                ## end 만나면 djk끝내기?
    # print([start,end],visited)
    return visited
n, e = map(int,input().split()) # 노드, 간선 개수
nodes = [[float('inf')]*(n+1) for _ in range(n+1)] # N**N 인접행렬
for _ in range(e):
    s, e, w = map(int,input().split())
    nodes[s][e] = min(nodes[s][e],w)
    nodes[e][s] = min(nodes[e][s],w)
v1, v2 = map(int,input().split())
# 출발점에서 v1 - v2 or v2-v1 이동후 n 이동?
### v1 - v2 바로연결된 간선을 무조건 지나는게 아니라,
### v1, v2 노드들을 순서로 지나기면 하면됨.
# 0 - v1 - v2 - n/ 0 - v2 - v1 - n
answer = float('inf')
dst0 = djk(1,n)
# 0 - v1 - v2 - n/
dst1 = djk(v1,n)
dst2 = djk(v2,n)
result1 = dst0[v1] + dst1[v2] + dst2[n]
# 0 - v2 - v1 - n/
result2 = dst0[v2] + dst2[v1] + dst1[n]
answer = min([answer,result1,result2])
if answer >= float('inf'):
    print(-1)
else:
    print(answer)