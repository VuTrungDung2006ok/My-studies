a = int(input("so dien ban dung trong thang la:"))
if 0 < a < 51:
    a = a * 1.678
    print("so tien ban phai tra la:",a)
elif 51 < a < 101:
    b = a - 50
    c = (50*1.678) + (b*1.734)
    print("so tien ban phai tra la:",c)
elif a > 100:
    b = a - 50
    c = b - 50
    d = (50 * 1.678)+(50*1.734)+(c *2.014)
    print("so tien ban phai tra la:",d)
