ABC=['@','A','B','C','D','E','F','G','H','I','J','K','L']
Nlist =[]
lst =[]
cnt = 0
for _ in range(5):   #입력하면서 숫자로 된 리스트 만들기
    a = input()
    for i in a:
        if i != '.':
            if i != 'x':
                for j in range(1,13):
                    if ABC[j] == i:
                        lst.append(j)
                        cnt += 1
            else:
                lst.append(0)
    Nlist.append(a)
idx=[
    [0,2,5,7],
    [1,2,3,4],
    [0,3,6,10],
    [7,8,9,10],
    [1,5,8,11],
    [4,6,9,11]
]

#각 자리 구하기
def find(x):
    if x == 12:
        for kk in idx:
            sumy = 0
            for k in kk:
                sumy += lst[k]
            if sumy != 26:
                return
        result.append(lst)
        return

    if lst[x] != 0:     #이미 값이 있는 자리면 넘어갔다가 돌아오면 리턴
        find(x+1)       #값이 있는자리에선 아무것도 안하게 만들었어야함..ㅜ
        return

    for ii in idx:      #혹시 중간에 완성된 한줄이 26이아니면 리턴
        sumidx=0
        s=0
        for jj in ii:
            if lst[jj] == 0:
                s = 1
                break
            else:
                sumidx += lst[jj]
        if s==0 and sumidx != 26:
            return

    for j in range(1,13):
        if j in lst:
            continue
        lst[x] = j
        find(x+1)
        if result:
            return
        lst[x] = 0

result=[]
find(0)


#출력
for yy in range(5):
    b=''
    for xx in range(9):
        if Nlist[yy][xx] == '.':
            b += '.'
        else:
            b += ABC[lst.pop(0)]
    print(b)