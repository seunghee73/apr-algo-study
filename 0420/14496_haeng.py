import heapq
start,end=map(int,input().split())
N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)

result=[999999999]*(N+1)
result[start]=0
ST=[]
heapq.heappush(ST,start)

while ST:
    A = heapq.heappop(ST)
    c = result[A]
    for i in road[A]:
        if result[i] > c+1:
            result[i] = c+1
            heapq.heappush(ST,i)

if result[end] == 999999999:
    print(-1)
else:
    print(result[end])