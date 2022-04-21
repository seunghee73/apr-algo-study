import heapq

N,M = map(int,input().split())
ward = list(map(int,input().split()))

road=[[] for _ in range(N)]
for _ in range(M):
    a,b,t = map(int,input().split())
    road[a].append([b,t])
    road[b].append([a,t])

result=[99999999999]*N
result[0]=0
ST=[]
ST.append([0,0])

while ST:
    now,cnt = heapq.heappop(ST)
    if cnt > result[now]:
        continue

    for i in road[now]:
        if i[0] != N-1 and ward[i[0]] == 1: continue
        if result[i[0]]> cnt+i[1]:
            result[i[0]] = cnt + i[1]
            heapq.heappush(ST, (i[0], cnt + i[1]))

if result[N-1] == 99999999999:
    print(-1)
else:
    print(result[N-1])
