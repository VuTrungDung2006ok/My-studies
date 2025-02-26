def nguyento(x):
    if x<2:
        return
    if x ==2 :
        return x
    if x >2:
        for i in range(2,int(x**0.5)+1):
            if x % i ==0:
                return
        return x

n,m= map(int,input().split())
a = []
b = []
for i in range(n,m+1):
    if nguyento(i) != None:
        a.append(i)
    for j in range(len(a)):
        if i % a[j] ==0 and i %(a[j]**2) ==0:
            b.append(i)

print(b)



        