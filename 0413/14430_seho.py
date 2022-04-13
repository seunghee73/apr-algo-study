n , m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
answer = [[0]*m for _ in range(n)]
answer[0][0] = board[0][0]
for col in range(1,m):
    answer[0][col] += board[0][col] + answer[0][col-1]
for row in range(1,n):
    answer[row][0] += board[row][0] + answer[row-1][0]

for row in range(1,n):
    for col in range(1,m):
        answer[row][col] = board[row][col]+max(answer[row-1][col],answer[row][col-1])

print(answer[n-1][m-1])