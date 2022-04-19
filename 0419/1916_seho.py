from collections import deque
import sys
input = sys.stdin.readline
## bfs 로 했을때 사이클에서 나오질 못해서 시간초과
## 같은 경로에 다른 가중치로 들어오는것에 대한 처리
def djk():
    global n, answer, nodes, vertexes, target

    while sum(vertexes) < n:
        minV = float('inf')
        minIdx = -1
        for idx in range(len(answer)):
            if answer[idx] < minV and vertexes[idx] == 0:
                minV = answer[idx]
                minIdx = idx
        vertexes[minIdx] = 1
        if minIdx == target-1:
            return

        for nxt in range(len(nodes[minIdx])):
            answer[nxt] = min(answer[nxt], answer[minIdx]+nodes[minIdx][nxt])

n = int(input())
answer = [float('inf')]*n
m = int(input())
nodes =[[float('inf')]*n for _ in range(n)]
for i in range(n):
    nodes[i][i] = 0
for _ in range(m):
    a, b, c = map(int,input().split())
    nodes[a-1][b-1] = min(nodes[a-1][b-1],c)
source, target = map(int,input().split())

vertexes = [0]*n
vertexes[source-1] = 1
for idx in range(n):
    answer[idx] = min(answer[idx],nodes[source-1][idx])

djk()
print(answer[target-1])