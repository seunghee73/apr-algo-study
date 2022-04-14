n = int(input())
fib = [0, 1]
cnt = 2
while cnt <= abs(n):
    fib.append((fib[cnt-1]+fib[cnt-2])%1000000000)
    cnt += 1
if n == 0:
    print(0)
elif n % 2 == 0 and n < 0:
    print(-1)
else:
    print(1)
print(fib[abs(n)])