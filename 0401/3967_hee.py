import string
Upper = '0' + string.ascii_uppercase
D = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'x': -1}

def chk(s): # 매직스타 조건 만족 체크
    if sum([D[s[0]], D[s[2]], D[s[5]], D[s[7]]]) != 26:
        return False
    if sum([D[s[1]], D[s[2]], D[s[3]], D[s[4]]]) != 26:
        return False
    if sum([D[s[1]], D[s[5]], D[s[8]], D[s[11]]]) != 26:
        return False
    if sum([D[s[7]], D[s[8]], D[s[9]], D[s[10]]]) != 26:
        return False
    if sum([D[s[4]], D[s[6]], D[s[9]], D[s[11]]]) != 26:
        return False
    if sum([D[s[0]], D[s[3]], D[s[6]], D[s[10]]]) != 26:
        return False
    return True

def hexagram(idx, s):
    global ans
    if s > ans[:idx]:
        return
    # 현재까지 문자열이 ans보다 사전 상 뒤에 있는 경우에는 return

    if idx == 12:
        if chk(s):
            ans = min(s, ans)
        return
    # 문자열 길이가 12일 때 ans 체크 후 return

    if lst[idx] != 'x':
        s += lst[idx]
        hexagram(idx + 1, s)
        return
    # 이미 입력받은 문자열인 경우에는 넣고 다음으로

    for i in range(12):
        if not V[i]:
            V[i] = True
            hexagram(idx + 1, s + Upper[i+1])
            V[i] = False
    # 넣을 수 있는 문자열 넣어서 다음으로

V = [False] * 12 # 사용한 문자열 체크
lst = [-1] * 12 # 입력받은 문자열 체크
idx = 0
ans = 'ZZZZZZZZZZZZ' # ans 초기화
for _ in range(5):
    l = input()
    for i in l:
        if i != '.':
            lst[idx] = i
            idx += 1
            if D[i] != -1:
                V[D[i]-1] = True
hexagram(0,'')

print(f'....{ans[0]}....')
print(f'.{ans[1]}.{ans[2]}.{ans[3]}.{ans[4]}.')
print(f'..{ans[5]}...{ans[6]}..')
print(f'.{ans[7]}.{ans[8]}.{ans[9]}.{ans[10]}.')
print(f'....{ans[11]}....')