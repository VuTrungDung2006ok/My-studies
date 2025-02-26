n = int(input("nhap so luong"))
a = []
b = 1
c = 1
for i in range(0,n):
    a.append(int(input()))
    for j in a:
        if j > 0:
            b*=j
        elif j < 0:
            c *=j
s = abs*(b-c)
print(s)
            



    

    