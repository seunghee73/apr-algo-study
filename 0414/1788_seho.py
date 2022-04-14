from collections import deque
n = int(input())
if n > 0:
    memo = deque([0]*2)
    memo[1] = 1
    for idx in range(2,n+1):
        memo.append(memo[1] + memo[0])
        memo.popleft()
    if memo[1] > 0:
        print(1)
    else:
        print(-1)
    print(abs(memo[1])%1000000000)
elif n < 0:
    memo = deque([0]*2)
    memo[0] = 1
    for idx in range(2,abs(n)+2):
        memo.append(memo[0]-memo[1])
        memo.popleft()
    if memo[1] > 0:
        print(1)
    else:
        print(-1)
    print(abs(memo[1])%1000000000)
else:
    print(0)
    print(0)