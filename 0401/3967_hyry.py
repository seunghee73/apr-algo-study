import sys
input = sys.stdin.readline

'''
문자가 들어갈 자리 (starlst) index
-> 사전 순서 유지 쉽게 하기 위해
....0....
.1.2.3.4.
..5...6..
.7.8.9.10.
....11....

'''


def makeStar(depth):
    global madeStar

    for (a, b, c, d) in pairs:
        if True == starlstused[a] == starlstused[b] == starlstused[c] == starlstused[d]:
            if starlst[a] + starlst[b] + starlst[c] + starlst[d] != 26:
                return 0

    if depth == 12:
        madeStar = starlst[::]  # 여기서 copy제대로 안해서 한 번 틀림
        # print(madeStar)
        return 1

    if starlstused[depth]:  # 이미 들어있다면 다음 자리로 넘기기
        if makeStar(depth + 1):
            return 1  # 여기서 return 안 해줘서 또 틀림

    else:
        # 1~12 순으로 숫자(=각 알파벳 A ~ L에 대응)가 들어가기 때문에
        # 굳이 여러 가능성을 따로 모아볼 필요 없이
        # 맨 처음 완성 되는 값이 사전 순으로 가장 앞이다
        for num in range(1, 12 + 1):
            if not used[num]:
                starlst[depth] = num
                used[num] = starlstused[depth] = True
                if makeStar(depth + 1):
                    return 1
                used[num] = starlstused[depth] = False


star = [[-1] * 9 for _ in range(5)]  # 안 들어 가는 곳 -1로 표시
starlst = [0] * 12  # star 자리 별 들어간 숫자
starlstused = [False] * 12  # starlst의 어느 인덱스가 사용됐는지
used = [False] * (12 + 1)  # 사용한 숫자 체크 0, 1 ~ 12

pairs = [  # 1, 2, 3, 4가 가장 먼저 나와야 컷이 빠르다
    (1, 2, 3, 4), (0, 2, 5, 7), (7, 8, 9, 10),
    (0, 3, 6, 10), (1, 5, 8, 11), (4, 6, 9, 11)
]

idx = 0
for i in range(5):
    tmp = input().rstrip()
    for j in range(9):
        if tmp[j] == '.':
            continue
        if tmp[j] == 'x':  # 들어갈 자리 0
            star[i][j] = 0
            idx += 1
        else:  # 기존에 있던 문자 -> 숫자로 치환해서 넣기
            num = ord(tmp[j]) - (ord('A') - 1)
            star[i][j] = num
            starlst[idx] = num
            starlstused[idx] = True
            used[num] = True
            idx += 1


madeStar = []
makeStar(0)
madeStar = list(map(lambda x: chr(x + 64), madeStar))
print(f'....{madeStar[0]}....')
print(f'.{madeStar[1]}.{madeStar[2]}.{madeStar[3]}.{madeStar[4]}.')
print(f'..{madeStar[5]}...{madeStar[6]}..')
print(f'.{madeStar[7]}.{madeStar[8]}.{madeStar[9]}.{madeStar[10]}.')
print(f'....{madeStar[11]}....')


'''
# 답 - 테케 순
1.

....A....
.H.B.I.G.
..K...J..
.L.C.E.F.
....D....

....x....
.H.x.x.x.
..x...J..
.L.x.x.F.
....x....

2.

....A....
.C.D.H.K.
..L...G..
.I.E.B.J.
....F....

....A....
.C.D.H.K.
..x...x..
.x.x.B.x.
....x....

'''

