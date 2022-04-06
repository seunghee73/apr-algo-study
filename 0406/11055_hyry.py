
N = int(input())
arr = list(map(int, input().split()))
memo = [0] * 1001

maxV = 0
for num in arr:
    memo[num] = max(memo[num], num + max(memo[:num]))
    if maxV < memo[num]:
        maxV = memo[num]

print(maxV)
