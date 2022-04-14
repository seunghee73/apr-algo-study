n = int(input())
DP = [0, 1]
if n == 0:
    print(0)
elif n % 2 == 0 and n < 0:
    print(-1)
else:
    print(1)
# 메모리 때문에 구할 때 1000000000으로 나눠준 다음 저장한다.
for i in range(2, abs(n)+1):
    DP.append((DP[i-1] + DP[i-2]) % 1000000000)
print(DP[abs(n)])
