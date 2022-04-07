A = int(input())
arr = list(map(int, input().split()))
visited = [1] * A
for i in range(A-2, -1, -1):
    for j in range(A-1, i, -1):
        if arr[j] < arr[i] and visited[j] + 1 > visited[i]:
            visited[i] = visited[j] + 1
print(max(visited))