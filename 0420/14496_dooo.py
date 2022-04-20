def bfs(x):
    q = []
    q.append(x)
    v[x] = 1
    while q:
        c = q.pop(0)
        if c == e:
            return v[e] -1
        for j in G[c]:
            if v[j] == 0:
                q.append(j)
                v[j] = v[c] + 1
    return -1


s, e = map(int, input().split())
n, m = map(int, input().split())
v = [0] * (n+1)
G = [[] for _ in range(n+1)]
for i in range(m):
    p1, p2 = map(int, input().split())
    G[p1].append(p2)
    G[p2].append(p1)
print(bfs(s))