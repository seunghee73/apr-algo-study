from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global nodes, answer
    queue = deque([a-1])

    while queue:
        tmp = queue.popleft()
        for nxt in nodes[tmp]:
            if answer[nxt] > answer[tmp] + 1 or answer[nxt] == -1:

                answer[nxt] = answer[tmp] + 1
                queue.append(nxt)

a, b = map(int,input().split())
n, m = map(int,input().split())
nodes = [[] for _ in range(n)]

for _ in range(m):
    s , e = map(int,input().split())
    nodes[s-1].append(e-1)
    nodes[e-1].append(s-1)
    ## 일방통행인지 양방통행인지 확인하기.
answer = [-1]*n
answer[a-1] = 0

bfs()
# print(answer)
if answer[b-1] >= n:
    print(-1)
else:
    print(answer[b-1])