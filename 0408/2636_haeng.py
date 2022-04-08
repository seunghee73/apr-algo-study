def air():
    ST=[]
    ST.append([0,0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited=[[False]*M for _ in range(N)]
    while ST:
        a,b=ST.pop(0)
        if lst[b][a] == 1:
            lst[b][a] = 0
            continue
        for i in range(4):
            X = a+dx[i]
            Y = b+dy[i]
            if 0<=X<M and 0<=Y<N and visited[Y][X] == False:
                ST.append([X,Y])
                visited[Y][X] = True

def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
    return cnt



N,M=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(list(map(int,input().split())))

ST=[]
A = check()
while A:
    ST.append(A)
    air()
    A = check()

print(len(ST))
print(ST[-1])