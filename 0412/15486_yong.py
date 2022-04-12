# 전 문제에서 데이터 수가 추가됐기 때문에 input방식을 변경
import sys
input = sys.stdin.readline

N = int(input())
arr = []
# 입력값을 arr에 리스트형태로 저장
for _ in range(N):
    arr.append(list(map(int, input().split())))
# 메모이제이션을 사용할 DP리스트 생성
DP = [0] * N
# 역순 참조를 위해 마지막 인덱스에 값을 정해준다.
if arr[-1][0] == 1:
    DP[-1] = arr[-1][1]
# 마지막 전 인덱스부터 0번째 인덱스까지 탐색 진행
for i in range(N-2, -1, -1):
    # 만약 그 인덱스에 상담을 진행해도 퇴사일 전일 때
    if i + arr[i][0]-1 < N:
        # 그 상담 이후에도 퇴사가 진행되지 않았으면 
        # val변수에 해당 인덱스 수입 + 상담 끝난 다음날에 해당하는 DP값 더해서 저장
        if i + arr[i][0] < N:
            DP[i] = arr[i][1] + DP[i+arr[i][0]]
        # 만약 그 상담이 마지막이라면 해당 수입만 저장
        else:
            DP[i] = arr[i][1]
    # 만약 DP값이 그 다음날의 DP값보다 작다면 값 변경
    if DP[i] < DP[i+1]:
        DP[i] = DP[i+1]

# 저장된 DP중 최대값 출력
print(max(DP))
