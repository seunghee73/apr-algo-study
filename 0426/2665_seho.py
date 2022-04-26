# 방 k개 뚫어서 목적지로 가는 경로찾기. k는 최소로 가져야함.
# n = 50. k <= 50. => djk*max(k) = n**3 = 12500
# 최소의 k 출력하기.
# n*n의 visited 각 칸은 검은방을 만난 횟수(= 검은방을 흰방으로 바꾼것
# 방문하지않았거나 이동했을때보다 더 작을때.
import sys
import heapq
def djk():
    global n, board, visited
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    visited[0][0] = 0
    queue = []
    heapq.heappush(queue,[0,[0,0]])

    while queue:
        cost,tmp = heapq.heappop(queue)
        for move in moves:
            nxtR = tmp[0] + move[0]
            nxtC = tmp[1] + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                nxtCost = 0
                if board[nxtR][nxtC] == 0:
                    nxtCost = 1
                if visited[nxtR][nxtC] == -1 or visited[nxtR][nxtC] > cost + nxtCost:
                    visited[nxtR][nxtC] = cost + nxtCost
                    heapq.heappush(queue,[visited[nxtR][nxtC],[nxtR,nxtC]])
input = sys.stdin.readline
n = int(input())
board = [list(map(int, list(input()[:-1]))) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

djk()
print(visited[n-1][n-1])