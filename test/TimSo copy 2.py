def tong(x):
    d = 0
    for i in range(1, x):
        if x % i ==0:
            d = d + i
    return d

n = int(input("nhap "))
for a in range(1, n+1):
     b = tong(a)
     if tong(b) == a and 1 <= a < b <= n:
        print(a,b)
     
         
     
    

        
        

    