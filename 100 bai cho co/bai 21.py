b = int(input("nhap so ngay"))
a = int(input("nhap so thang ban muon "))
c = 0
d = 0
f = 0
tong = 0
for i in range(1,a+1):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        d +=1
    elif i == 4 or i == 6 or i == 11 or i ==9:
        f +=1
    elif i == 2:
        c += 1

    tong = b + (31*d) + (30*f) + (28*c)

print("so ngay cach nam dau la", tong)
    