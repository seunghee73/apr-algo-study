n = int(input())
N=abs(n)

if n == 0:
    print(0)
    print(0)
else:  #만들다보니 음수의 경우 짝수자리만 자연수 피보나치에서 음수가 되는 규칙을 발견
    dp=[0] * (N+1)
    dp[1] = 1
    for i in range(2,N+1):
        dp[i] = (dp[i-1] + dp[i-2])%1000000000


    if n < 0 and n%2 == 0:
        print(-1)
        print(dp[N])
    else:
        print(1)
        print(dp[N])