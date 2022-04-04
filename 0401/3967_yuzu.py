import copy

num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6,
       'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12}
rev_num = dict(map(reversed, num.items()))

star = []
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = 0
for _ in range(5):
    s = list(input())
    for ss in s:
        if ss != '.':
            if ss == 'x':
                m += 1
                star.append(0)
            else:
                star.append(num[ss])
                num_lst.remove(num[ss])

ans = []
visited = [0]*m
n = m
def dfs(x, depth):
    global ans
    a = [star[0], star[2], star[5], star[7]]
    b = [star[1], star[2], star[3], star[4]]
    c = [star[7], star[8], star[9], star[10]]
    d = [star[4], star[6], star[9], star[11]]
    e = [star[1], star[5], star[8], star[11]]
    f = [star[0], star[3], star[6], star[10]]

    if depth == m:
        if sum(a) == 26 and sum(b) == 26 and sum(c) == 26 and sum(d) == 26 and sum(e) == 26 and sum(f) == 26:
            ans = copy.deepcopy(star)
        return

    for i in [a, b, c, d, e, f]:
        if 0 not in i and sum(i) != 26:
            return

    if ans:
        return
    for i in range(n):
        if visited[i] == 0:
            idx = star.index(0)
            star[idx] = num_lst[i]
            visited[i] = 1
            dfs(i+1, depth+1)
            star[idx] = 0
            visited[i] = 0

dfs(0, 0)
print('....%s....'%(rev_num[ans[0]]))
print('.%s.%s.%s.%s.'%(rev_num[ans[1]], rev_num[ans[2]], rev_num[ans[3]], rev_num[ans[4]]))
print('..%s...%s..'%(rev_num[ans[5]], rev_num[ans[6]]))
print('.%s.%s.%s.%s.'%(rev_num[ans[7]], rev_num[ans[8]], rev_num[ans[9]], rev_num[ans[10]]))
print('....%s....'%(rev_num[ans[11]]))