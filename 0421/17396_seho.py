import sys
import heapq
### 다익스트라 구현
### 일반 BFS 형식으로 리스트를 사용해 구현할 경우 -> n*n의 시간 복잡도.
### 우선순위 큐를 활용할 경우 -> n*logn의 시간복잡도 발생.
### 노드의 양방향 유무 체크/ 우선순위 큐 구현.

input = sys.stdin.readline
INF = float('inf')

def djk():
    global nodes, answer, siteLoc, n
    q = []
    ## 시작점은 0 이므로 힙큐를 통해 할당.
    heapq.heappush(q,(0,0)) ## (a,b)라 할때, 0에서 b까지 도달하는 최소 거리 a
    ## 0은 시작점이므로 최소도달 거리는 0이다.
    answer[0] = 0

    while q:
        dst, nowLoc = heapq.heappop(q)

        if answer[nowLoc] >= dst: ## 0에서 nowloc까지의 거리가 dst보다 작다면,
            for node in nodes[nowLoc]:
                nxt, cost = node  ## nowloc에 연결된 간선들 탐색.
                nxtCost = cost + dst
                if nxtCost < answer[nxt]: ## 간선을 타고 다음 이동 노드의 cost가 기존의 것보다 작다면,
                    answer[nxt] = nxtCost ## answer을 갱신하고 q에 추가한다.
                    heapq.heappush(q,(nxtCost,nxt))
    return

n , m = map(int,input().split())
nodes = [[] for _ in range(n)]
answer = [INF]*n

siteLoc = list(map(int,input().split()))
siteLoc[n-1] = 0
## 거치면 안되는 구간이 있으므로, 해당 구간의 노드 입력은 건너뛴다.
for _ in range(m):
    s, e, w = map(int,input().split())
    if siteLoc[e] == 0 and siteLoc[s] == 0:
        ## 노드는 양방향이므로 서로 추가
        nodes[s].append([e,w])
        nodes[e].append([s,w])

djk()

if answer[n-1] >= INF:
    print(-1)
else:
    print(answer[n-1])