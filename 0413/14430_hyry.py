import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 가로 누적
for col in range(1, M):
    arr[0][col] += arr[0][col - 1]

# 2. 세로 누적
for row in range(1, N):
    arr[row][0] += arr[row - 1][0]

# 3. 전체 누적
for row in range(1, N):
    for col in range(1, M):
        arr[row][col] = arr[row][col] + max(arr[row - 1][col], arr[row][col - 1])

print(arr[N - 1][M - 1])