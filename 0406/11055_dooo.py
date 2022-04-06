n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
total = 0
ans[0] = lst[0]

for i in range(1,n):

    j = 1
    max_val = lst[i]
    while j<=i:
        if lst[i] > lst[i-j]:
            cnt = lst[i] + ans[i-j]
            if cnt > max_val:
                max_val = cnt
            j += 1
        else:
            j += 1
    ans[i] = max_val

print(max(ans))