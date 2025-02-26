def nguyento(x):
    if x <2:
        return
    if x ==2:
        return x
    if x> 2:
        for i in range(2,int(x**0.5)+1):
            if x%i ==0:
                return
        return x
    
a =[]
so = int(input())
for j in range(so):
    n = int(input())
    for n1 in range(2, (n//2)+1):
        if nguyento(n1) != None:
            n2 = n - n1
            if nguyento(n2)!= None:
                a.append((n1,n2))

for k in a:
    print(f"{k[0]} {k[1]}")


