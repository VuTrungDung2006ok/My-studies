a = int(input())
b = input()
b = b.lower()
c = int(input())
kq = 0
if b == "tru":
    kq = a - c
elif b == "cong":
    kq = a + c
elif b == "chia":
    kq = a // c

print(bin(kq)[2:])
