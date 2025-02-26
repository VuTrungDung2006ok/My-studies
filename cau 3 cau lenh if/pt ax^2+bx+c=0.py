import math
a = float(input("a: ")) # ax^2+bx+c = 0
b = float(input("b: "))
c = float(input("c: "))
delta = b**2 - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh nay vo so nghiem")
        else:
            print("phuong trinh nay vo nghiem")
    else:
        x = -c/b
        print("phuong trinh nay co nghiem x =", x)
else:
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print("phuong trinh co 2 nghiem kep la x =", x)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("phuong trinh nay co 2 nghiem x1 va x2 =", x1 ,x2)

    
