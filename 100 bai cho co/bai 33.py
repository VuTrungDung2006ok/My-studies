a = int(input("nhap so cua ban: "))
b = 0
if a < 2: 
    print("day khong phai la so nguyen to")
else:
    for i in range (1,a):
        if a%i ==0:
            b +=1
    if b >= 2:
        print("day la khong phai la so nguyen to")
    elif b <2:
        print("day la so nguyen to")

    