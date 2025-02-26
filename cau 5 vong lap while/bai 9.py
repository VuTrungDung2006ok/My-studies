import random
so_may = random.randint(1, 101)
n = int(input("nhap so ban doan: "))
b = 0
while True:
    b += 1
    if n == so_may:
        print("ban da doan trung voi so lan la ", b)
        break
    else:
        print("ban doan chua dung")
        break

   

