def func():
    # 시작은 0, 0 / 방문표시 진행
    Q = [(0, 0)]
    visited[0][0] = 1
    # 1을 발견했을 때 바꿔줄 값을 저장할 변수 생성
    num = 2
    # 한 싸이클에서 목표로 하는 숫자를 리스트에 넣는다.
    # 표면부터 공기중에 녹을 때마다 2, 3, 4, 5 이렇게 바꿔주는데 그때마다 그 값을 target에 추가시킨다.
    # 0의 경우에는 치즈 속에도 숨어있어서 리스트 방식을 채용
    target = [0]
    while True:
        # 답을 찾는지 유무를 판단
        flag = 0
        # Q를 pop하지 않고 인덱스를 증가시켜가며 참조, 시간소모를 줄여보자
        i = 0
        # 다음에 싸이클에 탐색할 인덱스 정보를 n_Q에 저장시켜놓자
        n_Q = []
        # 해당 시간에 녹는 치즈량을 저장시키기위한 변수
        cnt = 0
        # i가 Q의 길이보다 커지면 더이상 찾을 내용이 없다는 뜻
        while i < len(Q):
            # Q에서 좌표 정보를 꺼내서 상하좌우 탐색
            y, x = Q[i]
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                # 인덱스 범위 안에 있고 방문하지 않았다면
                if 0 <= y+dy < N and 0 <= x+dx < M and not visited[y+dy][x+dx]:
                    # 만약 탐색한 좌표가 1(녹지 않은 치즈)이면 아래 과정을 진행시키자
                    if arr[y+dy][x+dx] == 1:
                        cnt += 1
                        # 이미 녹아 없어진 곳이라도 0으로 표현하면 구별이 힘드므로 다른 값을 대입하기로 했다.
                        # 시간마다 2, 3, 4, 5 이렇게 증가시킬 예정
                        arr[y+dy][x+dx] = num
                        # 다음 탐색 때 사용하기 위해 n_Q에 넣어두자
                        n_Q.append((y+dy, x+dx))
                    # 목표로 하는 값이라면 (처음에는 0 / 다음에는 0, 2 ...)
                    elif arr[y+dy][x+dx] in target:
                        # 방문표시를 하고 Q에 없는 좌표라면 추가시켜주자
                        # 치즈 속에 0이 숨어있어서 판단해줘야함
                        visited[y+dy][x+dx] = 1
                        if (y+dy, x+dx) not in Q:
                            Q.append((y+dy, x+dx))
            # 인덱스를 증가시켜 다음 탐색 진행
            i += 1
        # 반복문이 끝나면 1이 남았는지 판단, 1이 남아있다면 break
        for j in range(N):
            if 1 in arr[j]:
                flag = 1
                break
        # 일단 새로운 시작점에 방문표시 진행
        # n_Q에 저장된 다음 탐색지점을 deep_copy 후 target리스트를 갱신하자
        # 그리고 다음 싸이클에 녹은 치즈는 +1한 값으로 기록해두자
        if flag:
            visited[n_Q[0][0]][n_Q[0][1]] = 1
            Q = n_Q[::]
            target.append(num)
            num += 1
        # 1이 없다면 시간과 마지막 타임에 녹은 치즈량 반환
        else:
            return num-1, cnt



N, M = map(int, input().split())
# 입력데이터와 방문표시 저장
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
time, cnt = func()
print(time)
print(cnt)