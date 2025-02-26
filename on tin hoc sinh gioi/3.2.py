def sohoanhao(x):
    mau = []
    for i in range(1,x):
        if x % i == 0:
            mau.append(i)
    if sum(mau) == x:
        return x
    else:
        return 0

a = []
n, m = map(int,input().split())
for j in range(n,m+1):
    if sohoanhao(j) != 0:
        a.append(j)

print(" ".join(map(str,a)))
    
