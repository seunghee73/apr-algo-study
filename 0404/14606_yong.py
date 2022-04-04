def func(v):
    global ans
    # v가 1이면 리턴
    if v == 1:
        return
    # 반으로 나눈 값에 근접하는 쌍이 제일 크기 때문에 v//2와 v-V//2를 구한다
    ans += v//2 * (v - v//2)
    # 재귀함수 사용
    func(v//2)
    func(v - v//2)

N = int(input())
ans = 0
func(N)
print(ans)