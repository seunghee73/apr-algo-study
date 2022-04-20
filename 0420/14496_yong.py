from collections import deque
import sys
input = sys.stdin.readline

# 어제 진행한 다익스트라 문제와 같은 방식 마지막 -1출력 조심하자
def dijk():
    D = [1000000000] * (N+1)
    D[S] = 0
    cnt = 0
    q = deque([S])
    while cnt < N:
        V = q.popleft()
        visited[V] = 1
        for i in range(1, N+1):
            if not visited[i] and G[V][i]:
                if D[i] > D[V] + G[V][i]:
                    D[i] = D[V] + G[V][i]
        nextV = 0
        maxV = 1000000000
        for i in range(1, N+1):
            if not visited[i] and maxV > D[i]:
                nextV = i
                maxV = D[i]
        q.append(nextV)
        cnt += 1
    return D[E]

S, E = map(int, input().split())
N, M = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
ans = dijk()
if ans == 1000000000:
    print(-1)
else:
    print(ans)