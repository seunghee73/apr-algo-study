happy=[0]*11

happy[1] = 0
happy[2] = 1
for i in range(3,11):
    happy[i] = (i//2) * (i-i//2) + happy[i//2] + happy[i-i//2]

N=int(input())
print(happy[N])