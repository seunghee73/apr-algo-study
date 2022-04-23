import heapq
import sys
input = sys.stdin.readline
# 기존 다익스트라 알고리즘을 활용합니다.
# 방문하는 지점을 저장하는 visited리스트를 생성하여 이를 활용합니다.
def dijk(start):
    # 처음에 '-'로 구성된 리스트 생성
    visited = ['-'] * (N+1)
    D = [1000000000000000] * (N+1)
    D[start] = 0
    ans = [start]
    q = []
    # q에 이동한 경로를 저장할 ans라는 리스트를 함께 넣어줍니다.
    heapq.heappush(q, (0, start, ans))
    while q:
        d, now, way = heapq.heappop(q)
        if D[now] < d:
            continue
        else:
            for b, t in G[now]:
                if D[b] > t + d:
                    D[b] = t + d
                    # deepcopy를 활용해 리스트를 visited에 저장
                    copy_way = way[::]
                    copy_way.append(b)
                    visited[b] = copy_way
                    heapq.heappush(q, (t+d, b, copy_way))
    # 저장된 visited를 참조하며 각 인덱스에 저장된 객체를 if문 조건에 맞춰 출력
    for i in visited[1:N+1]:
        if i == '-':
            print(i, end=' ')
        else:
            print(i[1], end=' ')
    print()

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append((b, t))
    G[b].append((a, t))
# 출발점이 1 ~ N까지의 경우를 모두 탐색
for i in range(1, N+1):
    dijk(i)

