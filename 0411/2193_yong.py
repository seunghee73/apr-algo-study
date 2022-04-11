N = int(input())
# DP에 각 인덱스의 자리수일 때 끝이 0, 1인 이친수의 개수를 저장합니다.
DP = [(0, 0), (0, 1)]
# 이친수는 그 전 자리수의 이친수 정보로부터 append안의 결과를 얻을 수 있습니다.
for i in range(2, N+1):
    zero_cnt = DP[i-1][0]
    one_cnt = DP[i-1][1]
    DP.append((zero_cnt+one_cnt, zero_cnt))
print(sum(DP[N]))