from collections import deque

def bfs():
    global n, m, board, meltCnt
    visited = [[0]*m for _ in range(n)]
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([[0,0]])
    visited[0][0]= 1
    while queue:
        tmp = queue.popleft()
        for move in moves:
            row = tmp[0] + move[0]
            col = tmp[1] + move[1]
            ## 다음 이동 위치가 범위내에 있고, 방문하지 않았다면,
            if 0 <= row < n and 0 <= col < m and visited[row][col] == 0:
                ## 탐색위치에 치즈가 있다면,
                if board[row][col] == 1:
                    ## 치즈 녹이고 녹인 치즈 개수 추가
                    board[row][col] = 0
                    meltCnt += 1
                ## 치즈가 없다면,
                elif board[row][col] == 0:
                    ## 다음 탐색 위치에 추가
                    queue.append([row,col])
                ## 탐색을 했으므로 방문배열 체크.
                visited[row][col] = 1

####
n , m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

cheeseCnt = 0 ## 치즈 갯수 초기화
for r in range(n):
    cheeseCnt += sum(board[r])
time = 0 ## 흐르는 시간

while 1:
    time += 1 ## while 한바꾸에 1시간 추가
    meltCnt = 0 ## 녹은 치즈 갯수 초기화
    bfs()       ## (0,0) 부터 bfs로 탐색. 공기중에 닿아있는 치즈찾기.

    ## 치즈개수에서 녹여서 0이 되면 break
    if cheeseCnt - meltCnt == 0:
        break
    ## 아니면 녹이고 진행.
    else:
        cheeseCnt -= meltCnt

print(time)
print(cheeseCnt)

## 왜 오래 걸렸나.. 방문배열 체크를 잘못해서, 갔던곳 또가고를 반복함.
