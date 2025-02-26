n = int(input())
istr = str(n)
s = 0
while n<0:
    print("vui long nhap lai")
    n = int(input())
if n > 0:
    for i in istr:
        i = int(i)
        s += i

print(s)


