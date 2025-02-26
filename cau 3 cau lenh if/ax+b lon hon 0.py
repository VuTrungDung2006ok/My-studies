a = float(input("a: ")) # ax+b>0
b = float(input("b: "))
if a == 0:
    if b > 0:
        x = 0
        print("phuong trinh nay vo so nghiem")
    else:
        print("phuong trinh nay vo nghiem")
else:
    if b == 0:
        print("x>0 thi phuong trinh co nghiem")
    if b > 0:
        x = -b/a
        print("phuong trinh lon hon 0 khi x=", x)
    else:
        x = b/a
        print("phuong trinh lon hon 0 khi x=", x)


