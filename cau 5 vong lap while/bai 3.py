a = int(input("nhap so nguyen duong"))
while a < 0:
    print("nhap lai so nguyen duong")
    a = int(input("nhap so nguyen duong"))
b = 0
c = 0
if a > 0 : 
    while a > 0 : 
        a //= 10
        if a % 2 ==0:
            b += 1
        else:
            c += 1
print("n co so chan la",b,"va n co so le la",c)

