a = float(input("a: "))
b = float(input("b: "))
if a == 0 :
    if b == 0:
        print("phuong trinh nay vo so nghiem")
    else:
        print("phuong trinh nay vo nghiem")
else:
    x = -b/a
    print("phuong nay co 1 nghiem la x =", x)