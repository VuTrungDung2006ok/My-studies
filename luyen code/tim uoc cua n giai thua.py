def giai_thua(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d

t = int(input())
for i in range(t):
    a = int(input())
