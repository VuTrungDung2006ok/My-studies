a = float(input(" nhap so ban muon"))
b = float(input(" nhap so ban muon"))
c = float(input(" nhap so ban muon"))
if a < b < c:
    print("so nho nhat la", a)
    print("so lon nhat la", c)
elif a < c < b:
    print("so nho nhat la", a)
    print("so lon nhat la", b)
elif b < a < c:
    print("so nho nhat la", b)
    print("so lon nhat la", c)
elif b < c < a:
    print("so nho nhat la", b)
    print("so lon nhat la", a)
elif c < b < a:
    print("so nho nhat la", c)
    print("so lon nhat la", a)
elif c < a < b:
    print("so nho nhat la", c)
    print("so lon nhat la", b)