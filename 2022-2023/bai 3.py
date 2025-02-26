def nguyento(x):
    if x <2:
        return
    if x ==2:
        return x
    if x > 2:
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                return
        return x

soN, soM = map(int,input().split())
n = list(map(int,input().split()))
a = []
for i in range(soM):
    u, v = map(int,input().split())
    tong = 0
    for j in range(u-1,v):
        tong += n[j]    
    a.append(tong)

for k in a:
    if nguyento(k) != None:
        print(1)
    else:
        print(0)


