def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

n = int(input())
a=[]
b=[]
c=[]
for i in range(0,n):
    a.append(int(input()))

d = 0
f = 0
for i in a:
    if i == nguyento(i):
        d = i//2
        f = i - d
        b.append(d)
        c.append(f)
    else:
        
print(b, c)



        

