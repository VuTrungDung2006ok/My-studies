a = int(input("nhap so nguyen duong"))
while a < 0:
    print("nhap lai so nguyen duong")
    a = int(input("nhap so nguyen duong"))
b = 0
if a > 0 : 
    while a > 0 : 
        a //= 10 
        b += 1  
        
print(b)



    
    

    

