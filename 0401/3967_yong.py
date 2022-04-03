SumV = [[0, 2, 5, 7], [1, 2, 3, 4], [0, 3, 6, 10], [7, 8, 9, 10], [1, 5, 8, 11], [4, 6, 9, 11]]
# 12개의 결과를 입력했을 때 조건을 만족하나 확인, 답이면 사전순이기 때문에 먼저 나오는 결과가 답이 된다.
def check():
    for i in range(6):
        temp = 0
        for j in range(4):
            temp += ans[SumV[i][j]]
        if temp != 26:
            return False
    # 답이라면 True 반환
    return True

def find(cnt):
    global result
    # result가 True면 답을 찾은것이기 때문에 return 반복
    if result:
        return
    if cnt == 12:
        if check():
            result = True
            return
        else:
            return
    if ans[cnt]:
        find(cnt + 1)
    else:
        for v in range(1, 13):
            if not visited[v]:
                visited[v] = 1
                ans[cnt] = v
                find(cnt+1)
                if result:
                    return
                # 함수 결과로 result가 True가 되면 return
                ans[cnt] = 0
                visited[v] = 0

# 알파벳과 인덱스를 매칭
Alpha = ['x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
arr = []
ans = [0] * 12
result = False
s_lst = [[] for _ in range(6)]
# 방문표시 
visited = [0] * 13
cnt = 0
# arr배열에 입력값을 저장
for i in range(5):
    arr.append(list(input()))
# arr배열을 순회하여 .이 아닌 값을 발견할 때마다 순서대로 ans에 해당 문자 인덱스를 저장
for i in range(5):
    for j in range(9):
        if arr[i][j] != '.':
            ans[cnt] = Alpha.index(arr[i][j])
            visited[Alpha.index(arr[i][j])] = 1
            cnt += 1
find(0)
# 답출력
idx = 0
for i in range(5):
    for j in range(9):
        if arr[i][j] == '.':
            print(arr[i][j], end='')
        else:
            print(Alpha[ans[idx]], end='')
            idx += 1
    print()