N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for _ in range(1, N):
    arr[_][0] += arr[_-1][0]
for _ in range(1, M):
    arr[0][_] += arr[0][_-1]
for i in range(1, N):
    for j in range(1, M):
        if arr[i-1][j] >= arr[i][j-1]:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += arr[i][j-1]
print(arr[N-1][M-1])