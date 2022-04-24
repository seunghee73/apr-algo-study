import heapq
n,m = map(int,input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,input().split())
    road[a].append([b,t])
    road[b].append([a,t])

Y = []
for i in range(1,n+1):
    result = [[10000001,0] for _ in range(n+1)]
    result[i] = [0,'-']
    ST = []

    for j in road[i]:
        result[j[0]] = [j[1],j[0]]
        heapq.heappush(ST, (j[0],j[1],j[0]))
    while ST:
        now,cnt,first = heapq.heappop(ST)
        if cnt > result[now][0]:
            continue
        for k in road[now]:
            if result[k[0]][0] > cnt + k[1]:
                result[k[0]] = [cnt+k[1], first]
                heapq.heappush(ST, (k[0],cnt+k[1],first))

    Y1 = []
    for l in range(1,n+1):
        Y1.append(result[l][1])
    print(*Y1)

