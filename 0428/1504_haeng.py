import heapq

N,E = map(int,input().split())
road = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    road[a].append([b,c])
    road[b].append([a,c])
u,v = map(int,input().split())


def find(x):
    result=[8000001]*(N+1)
    result[x]=0

    ST=[[x,0]]

    while ST:
        now,cnt = heapq.heappop(ST)

        for i in road[now]:
            if result[i[0]] > cnt + i[1]:
                result[i[0]] = cnt + i[1]
                heapq.heappush(ST,(i[0], cnt+i[1]))
    return result


ST2=[]
y=999999999
def back(k,level,s): #이걸 굳이 백트래킹해봄
    global y
    if level == 2:
        l3 = find(k)[N]
        if y > s+l3:
            y = s+l3
        return
    for l in [u,v]:
        if l in ST2: continue
        a = find(k)[l]
        ST2.append(l)
        back(l,level+1,s+a)
        ST2.pop()
back(1,0,0)

if y >= 8000001:
    print(-1)
else:
    print(y)