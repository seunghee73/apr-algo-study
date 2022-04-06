n = int(input())
lst = list(map(int, input().split()))

total = 0
ans = lst[::]

for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            cnt = ans[i] + lst[j]
            if ans[i] < cnt:
                ans[i] =cnt
print(max(ans))