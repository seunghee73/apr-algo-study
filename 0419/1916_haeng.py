import sys
import heapq        #우선순위 큐 사용
input = sys.stdin.readline

N=int(input())
M=int(input())
Mlist=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    Mlist[a].append([b,c])
start,end=map(int,input().split())

result = [999999999]*(N+1)
result[start] = 0
ST=[]
ST.append([start,0])

while ST:
    A,cnt = heapq.heappop(ST)

    if cnt > result[A]:         #시간초과 원인?
        continue

    if Mlist[A]:
        for i in Mlist[A]:
            if result[i[0]] > cnt+i[1]:
                result[i[0]] = cnt +i[1]
                heapq.heappush(ST, (i[0],cnt+i[1]))

print(result[end])