n = int(input("nhap so"))
while n < 0:
    n = int(input("nhap so"))
a = 0
if n > 0 : 
    while n > 0 : 
        n //= 10
        a = a + n
print(a)