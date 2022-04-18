from collections import deque
N, M, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

ans = []
ST = deque([X])
V = [0] * (N+1)
V[X] = 0
while ST:
    x = ST.popleft()
    if V[x] == K:
        ans.append(x)
    for j in G[x]:
        if not V[j] and j != X:
            ST.append(j)
            V[j] = V[x] + 1
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)