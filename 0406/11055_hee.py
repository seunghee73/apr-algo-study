N = int(input())
A = list(map(int, input().split()))
DP = [0] * N
DP[0] = A[0]
for i in range(1,N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j])
    DP[i] += A[i]
print(max(DP))