
import sys
input = sys.stdin.readline


N = int(input())
memo = [0] * (N + 1)   
arr = []
for _ in range(N):
    T, P = map(int, input().split())
    arr.append((T, P))

for day in range(N - 1, -1, -1):
    end, money = arr[day]
    if day + end > N:  # 여기서 거르지 않고 처음부터 거르면 구멍이 난다 ㅠㅠ
        memo[day] = memo[day + 1]
    elif money <= memo[day + 1] - memo[day + end]:
        memo[day] = memo[day + 1]
    elif money > memo[day + 1] - memo[day + end]:
        memo[day] = memo[day + end] + money

print(memo[0])





