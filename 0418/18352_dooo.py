import sys
input=sys.stdin.readline
def bfs(x):
    q = []
    q.append(x)
    v[x] = 1
    while q:
        c = q.pop(0)
        for e in G[c]:
            if v[e] == 0:
                q.append(e)
                v[e] = v[c] +1


n, m, k, s = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    G[p1].append(p2)
v = [0] * (n+1)
bfs(s)
flag = False
for i in range(1, n+1):
    if v[i] == k+1:
        print(i)
        flag = True
if flag == False:
    print(-1)
