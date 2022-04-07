n = int(input())
lst = list(map(int,input().split()))
answer = [1]*n

for idx in range(n):
    maxV = 0
    for down in range(idx-1,-1,-1):
        if lst[down] > lst[idx]:
            if maxV < answer[down]:
                maxV = answer[down]
    answer[idx] += maxV
# print(answer)
print(max(answer))