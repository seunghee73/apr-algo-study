from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global x, nodes
    queue = deque([x-1])

    while queue:
        tmp = queue.popleft()
        for nxt in nodes[tmp]:
            if answer[nxt] == -1 or answer[nxt] >= answer[tmp]+1:
                answer[nxt] = answer[tmp]+1
                queue.append(nxt)

n, m, k, x = map(int,input().split()) # 도시개수, 도로개수, 거리정보,출발지점
nodes = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    nodes[a-1].append(b-1)

answer = [-1]*n
answer[x-1] = 1
bfs()
# print(answer)
result = []
for idx in range(len(answer)):
    if answer[idx] == k + 1:
        result.append(idx+1)
if result:
    for r in result:
        print(r)
else:
    print(-1)
