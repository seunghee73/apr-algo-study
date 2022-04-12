N = int(input())
T = []
P = []
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
lst = [0] * (N+1)
max_val = -1
for i in range(N):
    max_val = max(max_val, lst[i])
    if i + T[i] > N:
        continue
    lst[i+T[i]] = max(lst[i+T[i]], max_val + P[i])

print(max(lst))