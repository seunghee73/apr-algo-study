import heapq

N,M = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    road[a].append((b,c))
    road[b].append((a,c))

result = [50000001]*(N+1)
result[1]=0
ST=[[1,0]]

while ST:
    now,cnt = heapq.heappop(ST)

    for i in road[now]:
        if result[i[0]] > cnt + i[1]:
            result[i[0]] = cnt + i[1]
            heapq.heappush(ST,(i[0],cnt + i[1]))

print(result[N])