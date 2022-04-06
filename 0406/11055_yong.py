def func(idx, v, sumV):
    for i in range(idx+1, A):
        if arr[i] > v and memo[i] < sumV + arr[i]:
            memo[i] = sumV + arr[i]
            func(i, arr[i], sumV + arr[i])


A = int(input())
arr = list(map(int, input().split()))
memo = [0] * A
for i in range(A):
    if not memo[i]:
        memo[i] = arr[i]
        func(i, arr[i], arr[i])
print(max(memo))