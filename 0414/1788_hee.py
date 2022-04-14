import sys
input = sys.stdin.readline
n = int(input())
if n > 0: flag = True
else: flag = False

if n == 0:
    print(0)
    print(0)
    exit(0)

n = abs(n)
DP = [0] * (n+1)
for i in range(n+1):
    if i == 0 or i == 1:
        DP[i] = i % 10**9
    else:
        DP[i] = (DP[i-1] + DP[i-2]) % 10**9
if flag:
    print(1)
    print(DP[-1])
else:
    if n % 2:
        print(1)
        print(DP[-1])
    else:
        print(-1)
        print(DP[-1])

