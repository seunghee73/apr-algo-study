n = int(input())
lst = [0]*90
lst[0],lst[1] = 1, 1
if n <= 2:
    print(lst[n-1])
else:
    for idx in range(2,n):
        lst[idx] = lst[idx-1] + lst[idx-2]
    print(lst[n-1])
## 아하하 디피문제.
## 백트래킹으로 수열만들다 이상해서 점화식세웠더니 규칙을 찾았다 ^^..