import heapq

n = int(input())
Nlist = []
for _ in range(n):
    Nlist.append(input())

result=[[2501]*n for _ in range(n)]
result[0][0] = 0

ST = [[0,0,0]]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while ST:
    nowx,nowy,black = heapq.heappop(ST)

    for i in range(4):
        X = nowx + dx[i]
        Y = nowy + dy[i]
        if 0<=X<n and 0<=Y<n:
            if Nlist[Y][X] == '0':
                B = black + 1
            else: B = black

            if result[Y][X] > B:
                result[Y][X] = B
                heapq.heappush(ST, [X,Y,B])

print(result[n-1][n-1])

