a = int(input("nhap so km"))
b = 0
if a < 2:
    b = 10000
elif a > 1 and a <= 25:
    b = 10000 + (( a - 1 )*13000)
elif a > 25 and a <=120:
    b = 10000 + (24*13000) + ((a-25)*11000)
elif a > 120:
    b = 10000 + (24*13000) + (120*11000) - (b*(10/100))

print(b)

