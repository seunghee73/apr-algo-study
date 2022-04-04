n = int(input())

arr = [0] * 11
arr[1] = 0
arr[2] = 1
arr[3] = 3

for i in range(4, 11):
    arr[i] = arr[i - 1] + i - 1

print(arr[n])
