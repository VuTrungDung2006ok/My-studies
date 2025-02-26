toan = float(input("nhap diem taon: "))
ta = float(input("nhap diem tieng anh: "))
van = float(input("nhap diem van: "))
diem_trung_binh =(toan + ta + van)/3
if diem_trung_binh >= 8 and (toan or van) >=8 and ta >=6.5:
    print("ban la hoc sinh gioi")
elif diem_trung_binh >= 5 and (toan or van) >=5 and ta >=3.5:
    print("ban la hoc sinh trung binh")
elif diem_trung_binh >= 3.5 and (toan or van) >=3.5 and ta >=2:
    print("ban la hoc sinh yeu")
elif diem_trung_binh < 3.5 and (toan or van) < 3.5 and ta <2:
    print("ban la hoc sinh kem")


