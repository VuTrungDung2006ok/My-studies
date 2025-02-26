x1,x2=map(int,input().split())
lst=[]
while 2<=x1 and x2<=10**9:
    for i in range(1,9999):
        if i%x1==0:
            d=i
            if d%x2==0:
                lst.append(d)           
    break
bcnn=(min(lst))
a = bcnn // x1
b = bcnn // x2
print(bcnn)
print(a,b)