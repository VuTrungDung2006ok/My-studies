def nguyento(x):
    for i in range(2,x):
        if x % i ==0:
            return True
    return False

n = int(input("viet so luong so: "))
a = []
b = []
c = []
for i in range(1,n+1):
    a.append(int(input()))
for j in a:
    b.append(a.count(nguyento(j)))
    
print(b)