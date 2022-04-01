# 미완성

import sys
input = sys.stdin.readline

ARR = [list(input().strip('\n')) for _ in range(5)]
positions = [[1, 3, 6, 8], [1, 4, 7, 11], [8, 9, 10, 11], [2, 3, 4, 5], [2, 6, 9, 12], [5, 7, 10, 12]]
nums = [0] * 13  # 0인덱스 무시, 여기에 12개 숫자 담을 것
v = [False] * 13  # 방문처리

idx = 1
for i in range(5):
    for j in range(9):
        target = ARR[i][j]
        if target == 'x':
            idx += 1
        elif target.isupper():
            nums[idx] = ord(target) - 64
            v[ord(target) - 64] = True
            idx += 1

def is26(arr):
    for pos in positions:
        sumV = 0
        for i in pos:
            sumV += arr[i]
        if sumV != 26:
            return False
    return True

def f(k):
    global sol
    if k == 13:
        # print(nums)
        if is26(nums):
            sol = nums
        return
    if nums[k] != 0:
        f(k + 1)
    for i in range(1, 13):
        if not v[i]:
            v[i] = True
            nums[k] = i
            f(k + 1)
            v[i] = False
            nums[k] = 0

sol = []
f(1)
