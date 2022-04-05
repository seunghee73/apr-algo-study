## 1,1 에서 n,m으로 이동하는 경우의 수 구하기
## 방향은 우 하 우하대각선

n , m = map(int,input().split())
answer = [[0]*1000 for _ in range(1000)]
for i in range(1000):
    answer[i][0] = 1
    answer[0][i] = 1


moves = [[0,-1],[-1,-1],[-1,0]]
for row in range(1,n):
    for col in range(1,m):
        for move in moves:
            answer[row][col] += answer[row+move[0]][col+move[1]]
print(answer[n-1][m-1]%(10**9+7))