n, m = map(int, input().split())

k = max(n, m)

arr = [[0] * k for _ in range(k)]
for i in range(k):
    arr[i][0] = 1
    arr[0][i] = 1
for i in range(1, k):
    for j in range(1, k):
        arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j] + arr[i][j - 1]) % 1000000007
print(arr[n - 1][m - 1])
