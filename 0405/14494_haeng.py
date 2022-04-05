N,M = map(int, input().split())

lst = [[0] * N for _ in range(M)]

for y in range(M):
    for x in range(N):
        if y == 0:
            lst[y][x] = 1
        elif x == 0:
            lst[y][x] = 1

        else:
            lst[y][x] = lst[y][x-1] + lst[y-1][x-1] + lst[y-1][x]

print(lst[M-1][N-1]%1000000007)