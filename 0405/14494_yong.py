import sys
sys.setrecursionlimit(10000000)

def func(y, x):
    # y나 x가 1보다 작아질 경우에는 0을 리턴시킴
    if y < 1 or x < 1:
        return 0
    # 만약 메모이제이션 배열에 값이 있다면 그 값을 반환
    if memo[y][x] != 0:
        return memo[y][x]
    else:
    # 메모이제이션에 값이 없다면 재귀를 진행하고 구한 값은 배열에 입력
    # 이 때, 대각선을 기준으로 대칭이기 때문에 메모이제이션을 더 편하게 할 수 있다.
        a = (func(y-1, x) + func(y, x-1) + func(y-1, x-1)) % (10**9 + 7)
        memo[y][x] = a
        memo[x][y] = a
    # 구한값을 반환
    return a
    
# 메모이제이션을 위해 2차원 배열 생성
memo = [[0] * 1001 for _ in range(1001)]
# 점화식 생성을 위해 일부 케이스 값 구해서 입력
# 여기서 [2][2]는 없어도 괜찮음
memo[1][1] = 1
memo[1][2] = 1
memo[2][1] = 1
memo[2][2] = 3
n, m = map(int, input().split())
print(func(n, m))