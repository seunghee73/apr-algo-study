n = int(input())
lst = list(map(int,input().split()))
answer = [0]*n
answer[0] = lst[0]
## 모든 인덱스 순ㅎ회 n
for i in range(1,n):
    compa = lst[i]
    compb = 0
    comIdx = -1
    for down in range(i-1,-1,-1):
        if lst[down] < compa and answer[down] > compb:
            compb = answer[down]
            comIdx = down
    if comIdx != -1:
        answer[i] += lst[i]+answer[comIdx]
    else:
        answer[i] = lst[i]
# print(answer)
print(max(answer))