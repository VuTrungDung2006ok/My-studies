a = int(input("nhap so thang ban muon "))
b = int(input("nhap nam ban muon "))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("thang nay co 31 ngay")
elif a == 4 or a == 6 or a == 11 or a ==9:
    print("thang nay co 30 ngay")
if a == 2:
    if (b % 400 == 0) or (b % 4 == 0) and (b % 100 != 0):
        print("thang 2 co so ngay la 29")
    else:
        print("thang 2 co so ngay la 28")
   