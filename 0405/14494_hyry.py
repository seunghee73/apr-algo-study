n, m = map(int, input().split())
arr = [[1] * m for _ in range(n)]

for row in range(1, n):
    for col in range(1, m):
        arr[row][col] = arr[row][col - 1] + arr[row - 1][col] + arr[row - 1][col - 1]

print(arr[n - 1][m - 1] % 1_000_000_007)


n, m = map(int, input().split())
arr = [[1] * m for _ in range(n)]

for row in range(1, n):
    for col in range(1, m):
        arr[row][col] = (arr[row][col - 1] + arr[row - 1][col] + arr[row - 1][col - 1]) % 1_000_000_007

print(arr[n - 1][m - 1])