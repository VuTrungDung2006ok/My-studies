a = int(input())
b = int(input())
c = int(input())
d = 0
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print(" day la tam giac deu")
    elif (a**2) == b**2 + c **2 or (b**2) == a**2 + c**2 or (c**2) == a**2 + b**2:
        print("day la tam giac vuong")
    elif a == b and c**2 == b**2 + a**2 or a == c and b**2 == a**2 + c**2 or b == c and a**2 == c**2 + b**2:
        print("day la tam giac vuong can")
    elif b == c or b == a or a == c:
        print("day la tam giac can")
    else:
        print("day la tam giac thuong")
else:
    print("day khong phai la tam giac")


