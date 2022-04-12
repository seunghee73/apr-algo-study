import sys
input = sys.stdin.readline
N = int(input())
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))

DP = [0] * (N+1)
for i in range(N-1, -1, -1):
    time, reward = P[i]
    if i + time > N:
        DP[i] = DP[i + 1]
    else:
        DP[i] = max(DP[i + time] + reward, DP[i + 1])
print(DP[0])