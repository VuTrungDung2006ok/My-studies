a, b ,c = map(int,input().split())
denta = (b**2) - 4*a*c
if a == 0 and b == 0 and c == 0:
    print("WOW")
if denta < 0:
    print("NO")
else:
    if b == 0:
        print("NO")
    else:
        x1 = (-b-(denta**(1/2)))/2*a
        x2 = (-b+(denta**(1/2)))/2*a
        kq1 = round(x1, 2)
        kq2 = round(x2, 2)
        print(kq1, kq2)