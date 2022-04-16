def BFS(x,y,n):
    global result
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ST.append([x,y,n])
    visited[y][x]=True
    while ST:
        a,b,c = ST.pop(0)
        if c > result:
            result = c
        for i in range(4):
            X= a + dx[i]
            Y= b + dy[i]
            if 0<=X<M and 0<=Y<N and Nlist[Y][X]=='L' and visited[Y][X] ==False:
                ST.append([X,Y,c+1])
                visited[Y][X] = True


N,M=map(int,input().split())
Nlist=[]
for _ in range(N):
    Nlist.append(input())

result=0
for y in range(N):
    for x in range(M):
        if Nlist[y][x] == 'L':
            visited = [[False] * M for _ in range(N)]
            ST=[]
            BFS(x,y,0)

print(result)