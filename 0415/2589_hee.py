from collections import deque
N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(input()))

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
for i in range(M):
    for j in range(N):
        if G[j][i] == 'L':
            V = [[0] * M for _ in range(N)]
            ST = deque([(i, j)])
            V[j][i] = 1
            while ST:
                x, y = ST.popleft()
                for d in D:
                    nx = x + d[0]
                    ny = y + d[1]
                    if -1 < nx < M and - 1 < ny < N and not V[ny][nx] and G[ny][nx] == 'L':
                        ST.append((nx, ny))
                        V[ny][nx] = V[y][x] + 1
                        if V[ny][nx] > ans:
                            ans = V[ny][nx]
print(ans-1)
