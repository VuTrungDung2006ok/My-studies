t = int(input())
kq = []
for i in range(t):
    x, y, n = map(int, input().split())
    if y > n % x:
        kq.append(n - n % x - x + y)
    else:
        kq.append(n - n % x + y)
for i in kq:
    print(i)