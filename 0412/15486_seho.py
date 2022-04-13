import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
answer = [0]*(n+1)
maxV = 0
for idx in range(n):
    nxt = idx + lst[idx][0]-1
    if nxt < n:
        answer[nxt] = max(answer[nxt],answer[idx-1]+lst[idx][1])
    answer[idx] = max(answer[idx],answer[idx-1])
print(max(answer))