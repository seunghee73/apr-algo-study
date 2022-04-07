N = int(input())
arr = list(map(int, input().split()))
memo = [0] * 1002

for num in arr:
    memo[num] = max(memo[num + 1:]) + 1

print(max(memo))
