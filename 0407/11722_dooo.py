n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
ans[0] = 1
lst = lst[::-1]
sol = [0]
for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j]:
            sol.append(ans[j])
    ans[i] += 1 + max(sol)
    sol = [0]

print(max(ans))