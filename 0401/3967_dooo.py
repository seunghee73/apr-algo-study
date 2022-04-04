def perm(n, k):
    global flag
    if n == k:
        total1 = arr[0][4] + arr[1][3] + arr[2][2] + arr[3][1]
        total2 = sum(arr[3])
        total3 = arr[0][4] + arr[1][5] + arr[2][6] + arr[3][7]
        total4 = sum(arr[1])
        total5 = arr[1][7] + arr[2][6] + arr[3][5] + arr[4][4]
        total6 = arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4]
        if total1 == 26 and total2 == 26 and total3 == 26 and total4 == 26 and total5 == 26 and total6 ==26:
            for r1 in range(5):
                for r2 in range(9):
                    if arr[r1][r2] == 0:
                        arr[r1][r2] = '.'
                    else:
                        arr[r1][r2] =str_dic[arr[r1][r2]]
            if flag == False:
                for rr in range(5):
                    for cc in range(9):
                        print(arr[rr][cc],end='')
                    print()

                flag = True
            return
        return

    for i in num_dic.values():
        if flag == True:
            return
        if v[i] == 0:
            v[i] = 1
            arr[lst[n][0]][lst[n][1]] = i
            perm(n+1, k)
            v[i] = 0

num_dic = {'A' : 1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12}
str_dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L'}
arr = [list(input()) for _ in range(5)]
v = [0] * 13
lst = []
for i in range(5):
    for j in range(9):
        if arr[i][j] == 'x':
            lst.append([i, j])
for i in arr:
    for j in range(len(i)):
        if i[j] in num_dic.keys():
            i[j] = num_dic[i[j]]
            v[i[j]] = 1
        else:
            i[j] = 0
flag = False
perm(0, len(lst))
