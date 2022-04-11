N=int(input())

dp = [0]*(N+1)
dp[1]=1
a=1   # 끝자리 숫자가 1인경우
b=0   # 끝자리 숫자가 0인경우

#이전꺼의  끝자리 숫자가 1일경우 +  끝자리 숫자가 0인경우*2
for i in range(2,N+1):
    dp[i] = a + b*2
    a,b = b, a+b

print(dp[N])