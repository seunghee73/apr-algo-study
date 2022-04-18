import sys
from collections import deque

N,M,K,X = map(int,sys.stdin.readline().rstrip().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    road[a].append(b)

result=[300001]*(N+1)
result[X] = 0
q= deque()
q.append(X)
visited=[False]*(N+1)

while q:
    now = q.popleft()
    c = result[now]

    if road[now]:
        for i in road[now]:
            if visited[i] == False:
                if result[i] > c+1:
                    result[i]=c+1
                q.append(i)
                visited[i] = True


#출력
if K in result:
    for i in range(N+1):
        if result[i] == K:
            print(i)
else:
    print(-1)