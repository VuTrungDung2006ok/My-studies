def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

d = 0
n = int(input())
a = list(map(int,input().split()))
for i in a:
    if
