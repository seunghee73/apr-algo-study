import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    Q = deque()
    Q.append(X)
    visited = [0 for _ in range(N + 1)]
    visited[X] = 1

    while Q:
        curCity = Q.popleft()

        for nexCity in adj[curCity]:
            if not visited[nexCity]:
                Q.append(nexCity)
                visited[nexCity] = visited[curCity] + 1
                if visited[curCity] == K:
                    cities.append(nexCity)


# 정점 개수, 엣지 개수, 찾는 거리, 출발 도시 X
N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]  # 도시 번호 1번 부터
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
cities = []
bfs()
cities.sort()
if cities: print(*cities, sep='\n')
else: print(-1)
