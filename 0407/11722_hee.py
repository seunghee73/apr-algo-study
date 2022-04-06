N = int(input())
A = list(map(int, input().split()))
DP = [0] * N
for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            DP[i] = max(DP[i], DP[j])
    DP[i] += 1
print(max(DP))