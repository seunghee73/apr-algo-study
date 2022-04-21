import heapq
import sys
input = sys.stdin.readline
# 다익스트라를 힙큐로 풀어야하는 문제, 자세한 원리는 분석이 필요합니다...
def dijk():
    D = [1000000000000000] * N
    D[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        d, now = heapq.heappop(q)
        if D[now] < d:
            continue
        else:
            for b, t in G[now]:
                if not visited[b] and D[b] > t + d:
                    D[b] = t + d
                    heapq.heappush(q, (t+d, b))
    return D[-1]

N, M = map(int, input().split())
visited = list(map(int, input().split()))
visited[-1] = 0
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append((b, t))
    G[b].append((a, t))
a = dijk()
if a == 1000000000000000:
    print(-1)
else:
    print(a)

# G를 1차원 배열
# deque를 그냥 q