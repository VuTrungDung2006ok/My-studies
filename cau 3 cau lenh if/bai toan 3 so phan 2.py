a = float(input(" nhap so ban muon"))
b = float(input(" nhap so ban muon"))
c = float(input(" nhap so ban muon"))
if a < b < c:
    print(a, b , c)
elif a < c < b:
    print(a, c , b)
elif b < a < c:
    print(b, a , c)
elif b < c < a:
    print(b, c , a)
elif c < b < a:
    print(c, b , a)
elif c < a < b:
    print(c, a, b)