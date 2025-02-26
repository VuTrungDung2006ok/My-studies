def nguyento(x):
    if x < 2:
        return
    if x == 2:
        return x
    if x > 2:
        for i in range(2,int(x**0.5)+1):
            if x % i ==0:
                return
        return x
    
so = int(input())
b = []
for i in range(so):
    n = int(input())
    a = []
    for j in range(1,n+1):
        if n % j == 0 and nguyento(j) != None:
            a.append(j)
    b.append(a)

for k in b:
    print(max(k))

