import sys
input = sys.stdin.readline

def f(S, N):
    u = [0] * (N + 1)
    u[S] = 1

    for i in range(N + 1):
        d[i] = adj[S][i]

    for _ in range(N):
        w = 0
        minV = INF
        for i in range(N + 1):
            if u[i] == 0 and minV > d[i]:
                minV = d[i]
                w = i
        u[w] = 1
        for v in range(N + 1):
            if -1 < adj[w][v] < INF:
                d[v] = min(d[v], d[w] + adj[w][v])

N = int(input().rstrip())
M = int(input().rstrip())
INF = 100000000
adj = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a][b] = min(adj[a][b], w)
for i in range(N + 1):
    adj[i][i] = -1
S, E = map(int, input().split())
d = [-1] * (N + 1)
f(S, N)
# print(d)
print(d[E])
