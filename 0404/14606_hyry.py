

# def joy(N):
#     return joy(N - 1) + (N - 1)

def joy(N):
    if N > 1 and not pizza[N]:
        pizza[N] = joy(N - 1) + (N - 1)
    return pizza[N]


N = int(input())
pizza = [0] * (N + 1)  # 0, 1 ~ 10

print(joy(N))
