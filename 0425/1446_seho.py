# 일방향/ D 이동. 중간에 점프 있음(점프비용있음)
# dp;

n, d = map(int,input().split())
nodes = [[] for _ in range(10001)]

for _ in range(n):
    s, e, w = map(int,input().split())
    if nodes[s]:
        nodes[s].append([e,w])
    else:
        nodes[s] = []
        nodes[s].append([e,w])
dst = [ i for i in range(10001)]
loc = 0
while loc < d:
    if nodes[loc]:
        for node in nodes[loc]:
            dst[node[0]] = min(dst[loc]+node[1],dst[node[0]])
    dst[loc+1] = min(dst[loc]+1,dst[loc+1])
    loc += 1
print(dst[d])
