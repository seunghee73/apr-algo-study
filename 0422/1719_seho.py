# n개의 노드가 있고, 각 노드에서 다른 노드로 향하는 최단경로를 구할때
# 각 다른 노드로 향할때 제일 먼저 방문해야하는 노드가 표시된 경로표 구하기.
# n개의 모든 노드에 대해 n-1개의 다른노드까지 최단거리 구하기?..
# 그러면서 방문해야할 노드 구하기?..
import sys
INF = float('inf')
input = sys.stdin.readline

def djk(start):
    global n, nodes, result
    dst = [INF] * n  ## 노드까지 현재 최소경로
    vertices = [0] * n  ## 현재 경로 확정된 노드
    way = [[] for _ in range(n)]  ## 경로 기록.
    dst[start] = 0
    vertices[start] = 1
    ## 초기값 갱신
    for idx in range(n):
        if nodes[start][idx] != -1:
            dst[idx] = nodes[start][idx]
            way[idx].append(idx)

    while sum(vertices) < n:
        # print(dst,vertices,way)
        minV = INF
        minIdx = -1
        for idx in range(n):
            if minV > dst[idx] and vertices[idx] == 0:
                minV = dst[idx]
                minIdx = idx
        if minIdx != -1:
            vertices[minIdx] = 1
        else:
            break
        for idx in range(n):
            if nodes[minIdx][idx] != -1 and dst[idx] > dst[minIdx] + nodes[minIdx][idx]:
                dst[idx] = dst[minIdx] + nodes[minIdx][idx]
                way[idx] = way[minIdx].copy()
                way[idx].append(idx)
    # print(dst, vertices, way)
    ## start에서부터 탐색
    for idx in range(n):
        if way[idx]:
            if len(way[idx]) >= 1: ## result의 가로 채우기
                result[start][idx] = way[idx][0]+1
                if len(way[idx]) == 1:
                    result[idx][start] = start + 1
                elif len(way[idx]) >= 2: ## result의 세로 채우기
                    result[idx][start] = way[idx][-2] + 1

# n <= 200/ n*(n*n) = 8,000,000(n개의 각 노드에서 bfs 실행)
n, m = map(int,input().split())
# 양방향 그래프. n도 작으니 인접행렬구현
nodes = [[-1]*n for _ in range(n)]
for _ in range(m):
    s, e, w = map(int,input().split())
    nodes[s-1][e-1] = w
    nodes[e-1][s-1] = w

result = [["-"]*n for _ in range(n)] ## 출력 결과

for idx in range(n):
    # print(idx)
    djk(idx)

for kk in range(n):
    print(*result[kk])