import sys
input = sys.stdin.readline


def bfs():
    Q = [a]
    visited = [0] * (N + 1)
    visited[a] = 1

    while Q:
        curV = Q.pop(0)
        if curV == b: return visited[curV] - 1
        for nexV in adj[curV]:
            if not visited[nexV]:
                Q.append(nexV)
                visited[nexV] = visited[curV] + 1

    return -1


a, b = map(int, input().split())
N, M = map(int, input().split())  # 전체 문자수, 치환 가능한 문자 쌍
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(bfs())
