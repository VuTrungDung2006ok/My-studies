def nguyento(x):
    if x < 2:
        return
    if x == 2:
        return x
    if x > 2:
        for i in range(2, int(x**0.5)+1):
            if x % i ==0:
                return
        return x
    
num = int(input())
d =[]

for i in range(num):
    n , m = map(int,input().split())
    kq = []
    for i in range(n, m+1):
        if nguyento(i) != None:
            kq.append(i)

    c = []
    mau ={1,4,6,8,9,0}
    
    for j in kq:
        b = []
        while j > 0:
            sodu = j % 10
            b.append(sodu)
            j = j // 10
        if not any(k in mau for k in b):
            c.append(b)
    d.append(len(c))

for dung in d:
    print(dung)
    
        



            

