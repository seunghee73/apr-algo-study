import heapq

T = int(input())
for t in range(T):
    n,d,c = map(int,input().split())
    road=[[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        road[b].append([a,s])

    result = [10000001]*(n+1)
    result[c] = 0
    ST = [[c,0]]

    while ST:
        now,sec = heapq.heappop(ST)

        for i in road[now]:
            if result[i[0]] > sec+i[1]:
                result[i[0]] = sec+i[1]
                heapq.heappush(ST,(i[0], sec+i[1]))
    cnt = 0
    Y = 0
    for j in range(1,n+1):
        if result[j] != 10000001:
            cnt +=1
            if result[j] > Y:
                Y = result[j]
    print(cnt,Y)
