# 결과물을 오름차순으로 내야하기 때문에 리스트를 하나 생성해서 리턴할 계획
# 평범한 bfs
def bfs():
    ans = []
    Q = [(X-1, 0)]
    visited[X-1] = 1
    while Q:
        idx, cnt = Q.pop(0)
        if cnt == K:
            ans.append(idx+1)
            continue
        if cnt > K:
            continue
        for i in G[idx]:
            if not visited[i]:
                Q.append((i, cnt+1))
                visited[i] = 1
    return ans    

N, M, K, X = map(int, input().split())
visited = [0] * N
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
ans = bfs()
# 리스트가 비어있냐 아니냐로 출력 결정
if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)    

# 아래는 다익스트라 복습겸 트라이...시초났습니다~~
# def dijk():
#     U = []
#     D = [1000000] * N
#     D[X-1] = 0

#     탐색위치 찾는 과정
#     while len(U) < N:
#         minV = 1000000
#         for i in range(N):
#             if i in U:
#                 continue
#             if minV > D[i]:
#                 curV = i
#                 minV = D[i]
        
#         U.append(curV)

#         탐색위치 기준 연결된 곳의 거리 확인
#         for i in range(N):
#             if i in U:
#                 continue
#             if G[curV][i]:
#                 if D[i] > D[curV] + G[curV][i]:
#                     D[i] = D[curV] + G[curV][i]
#     return D

# N, M, K, X = map(int, input().split())
# 단방향 그래프
# G = [[0] * N for _ in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     G[a-1][b-1] = 1
# arr = dijk()
# ans = []
# for i in range(len(arr)):
#     if arr[i] == K:
#         ans.append(i+1)
# if ans:
#     for i in ans:
#         print(i)
# else:
#     print(-1)