w = float(input("can nang(kg):"))
m = float(input("chieu cao(m)"))
suc_khoe = w/m**2
if suc_khoe < 18.5:
    print("gay")
elif 18.5 < suc_khoe < 30:
    print("binh thuong")
elif 25 < suc_khoe < 30:
    print("hoi beo")
elif 30 < suc_khoe < 35:
    print("beo phi cap do 1")
elif 35 < suc_khoe < 40:
    print("beo phi cap do 2")
elif suc_khoe > 40:
    print("beo phi cap do 3")
    
