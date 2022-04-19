import sys
input = sys.stdin.readline
from collections import deque

# 처음으로 맞은 정답, in을 사용해서 시간이 너무 걸려 단축이 필요하다, visited생성할 필요 존재
# def dijk():
#     D = [10000000000] * (N+1)
#     U = [S]
#     D[S] = 0
#     q = deque([S])
#     while len(U) <= N:
#         V = q.popleft()
#         for i in range(1, N+1):
#             if i not in U and city[V][i] >= 0:
#                 if D[i] > D[V] + city[V][i]:
#                     D[i] = D[V] + city[V][i]
#         nextV = 0
#         maxV = 10000000000
#         for i in range(1, N+1):
#             if i not in U and maxV > D[i]:
#                 maxV = D[i]
#                 nextV = i
#         U.append(nextV)
#         q.append((nextV))
#     return D[E]

# 시간 단축 가자~~~
def dijk():
    D = [10000000000] * (N+1)
    D[S] = 0
    q = deque([S])
    cnt = 0
    while cnt < N:
        V = q.popleft()
        visited[V] = 1
        for i in range(1, N+1):
            if not visited[i] and city[V][i] >= 0:
                if D[i] > D[V] + city[V][i]:
                    D[i] = D[V] + city[V][i]
        nextV = 0
        maxV = 10000000000
        for i in range(1, N+1):
            if not visited[i] and maxV > D[i]:
                maxV = D[i]
                nextV = i
        cnt += 1
        q.append((nextV))
    return D[E]

N = int(input())
M = int(input())
city = [[-1] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
# 같은 루트여도 다른 비용의 버스가 존재해서 최소값을 받아준다.
for _ in range(M):
    s, e, b = map(int, input().split())
    if city[s][e] == -1:
        city[s][e] = b
    elif city[s][e] > b:
        city[s][e] = b
S, E = map(int, input().split())
print(dijk())