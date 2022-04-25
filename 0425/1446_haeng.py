N,D = map(int,input().split())
road = [[] for _ in range(D+1)]
for _ in range(N):
    a,b,c = map(int,input().split())
    if b > D:
        continue    #역주행방지
    road[a].append([b,c])


result = [D+1]*(D+1)
result[0] = 0
for i in range(0,D+1):
    if i != 0 and result[i] > result[i-1]+1:
        result[i] = result[i-1]+1

    for j in road[i]:
        if result[j[0]] > result[i]+j[1]:
            result[j[0]] = result[i]+j[1]

print(result[D])