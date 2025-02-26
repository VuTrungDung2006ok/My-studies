with open('Py3P1.IN .txt','r') as file:
    lines = file.readlines()

kq = []

for i in range(0,len(lines),1):
    n = int(lines[i].strip())

    tong = 0
    if n > 0 and n <= 50:
        tong = 1000*(n)
    elif n > 50 and n <= 100:
        tong = 50000 + ((n-50) * 1200)
    elif n > 100 and n <= 200:
        tong = 50000 + 60000 +((n-100) * 1500)
    elif n > 200 and n <=300:
        tong = 50000 + 60000 + 150000 + ((n-200) * 2000)
    elif n > 300:
        tong = 50000 + 60000 + 150000 + ((n-200) * 2000)
        tong = tong - (tong*5//100)

    kq.append(str(tong))


with open('Py3P1.OUT.txt','w') as file:
    file.write("\n".join(kq) + "\n")