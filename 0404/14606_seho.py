def splitPizza(get_):
    global answer
    if get_ not in [0,1]:
        left,right = get_//2, get_-get_//2
        answer += left*right
        splitPizza(left)
        splitPizza(right)


n = int(input())
answer = 0
splitPizza(n)
print(answer)
