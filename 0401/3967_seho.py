# print(ord("A")-64)
# 1 ~ 12
def fulfill(loc):
    global lst,fixIdx,answer
    if not answer:
        line1 = [lst[0], lst[2], lst[5], lst[7]]
        line2 = [lst[0], lst[3], lst[6], lst[10]]
        line3 = [lst[1], lst[2], lst[3], lst[4]]
        line4 = [lst[1], lst[5], lst[8], lst[11]]
        line5 = [lst[4], lst[6], lst[9], lst[11]]
        line6 = [lst[7], lst[8], lst[9], lst[10]]
        lines = [line1, line2, line3, line4, line5, line6]
        for line in lines:
            if sum(line) > 26:
                return
        if loc == 12:
            answer = lst.copy()
        if loc not in fixIdx:
            for i in range(1,13):
                if i not in lst and lst[loc] == 0:
                    lst[loc] = i
                    fulfill(loc+1)
                    lst[loc] = 0
        else:
            fulfill(loc+1)
    else:
        return


board = [list(input()) for _ in range(5)]
lst = []
fixIdx = []
for row in range(5):
    for col in range(len(board[0])):
        if board[row][col] != ".":
            if board[row][col] == "x":
                lst.append(0)
            else:
                lst.append(ord(board[row][col])-64)
for i in range(len(lst)):
    if lst[i] != 0:
        fixIdx.append(i)

### 채워져있는곳 제외하고 나머지 공간 채우는거 구현
answer = []
fulfill(0)
# answer.sort()

for row in range(5):
    for col in range(9):
        if board[row][col] != ".":
            board[row][col] = chr(answer.pop(0)+64)
for kk in board:
    print("".join(kk))
