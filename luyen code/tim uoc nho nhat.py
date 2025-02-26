def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

def timuoclonnhat(n):
    b = []
    for i in range(1, n):
        if n % i == 0 and n % 2 == 1:
            b.append(i)
    return max(b)

t = int(input())
a = []
tong = []
for i in range(t):
    n = int(input())
    a.append(n)

for j in a:
    if nguyento(j):
        tong.append(1)
    else:
        if j % 2 ==0:
            while j %2 ==0:
                j = j // 2
            tong.append(j)
        else:
            tong.append(timuoclonnhat(j))

for k in tong:
    print(k)
