# DP를 활용하여 쉽게 풀 수 있는 문제
# 데이터의 개수가 최대 12개밖에 없기 때문에 배열을 생성하기에는 메모리가 아깝다고 생각
# 딕셔너리에 저장하여 메모리와 시간을 아껴보려는 전략
dic = {

}

N, M = map(int, input().split())
DP = [0] * (M+1)
for i in range(N):
    s, e, d = map(int, input().split())
    if e <= M:
        try:
            dic[s].append((e, d))
        except:
            dic[s] = [(e, d)]
# 0 일때만 0을 넣고 그 외에는 조건에 따라 값을 대입
# 그리고 해당 idx가 딕셔너리 키라면 지름길 거리도 적어두기
for i in range(0, M+1):
    if i == 0:
        DP[i] = 0
    elif not DP[i] or DP[i] > DP[i-1] + 1:
        DP[i] = DP[i-1] + 1
    if i in dic.keys():
        for val in dic[i]:
            if not DP[val[0]] or DP[val[0]] > DP[i] + val[1]:
                DP[val[0]] = DP[i] + val[1]
print(DP[-1])

