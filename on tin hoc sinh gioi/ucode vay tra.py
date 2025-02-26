def trano(i):
    global tong_am, tong_duong, d , vitri
    tong_duong += tong_am
    tong_am = 0
    d += (i-vitri)*2
    vitri = -1

n = int(input())
a = list(map(int,input().split()))
s = sum(a)
if s <= 0: # quang duong
    d = n 
else:
    tong_duong = 0 # so tien thu duoc
    tong_am = 0 # so tien phai tra
    d = 1
    vitri = -1 # cua ngoi nha dau tien van con no
    for i in range(n):
        d += 1 # moi lan di toi nha moi la d tang len 1
        if a[i] > 0:
            tong_duong += a[i]
        elif a[i] < 0:
            if vitri == -1:
                vitri = i
            tong_am += a[i]
        if abs(tong_duong) >= abs(tong_am):
            trano(i) 
    
print(d)