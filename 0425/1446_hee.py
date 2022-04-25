N, D = map(int, input().split())

G = []
for _ in range(N):
    S, E, P = map(int, input().split())
    G.append((S, E, P))
G.sort() # 정렬 매우 중요

DP = [i for i in range(D+1)]

for s, e, p in G:
    if e > D:
        continue
    if DP[e] > DP[s] + p:
        DP[e] = DP[s] + p
        for j in range(e+1, D+1):
            if DP[j-1] + 1 < DP[j]:
                DP[j] = DP[j-1] + 1

print(DP[-1])