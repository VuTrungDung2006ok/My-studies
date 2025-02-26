gao = int(input("so gao me cho: "))
for i in range(0, gao//5 + 1):
    for j in range(0 ,gao//3 + 1):
        if (i*5)+(j*3) == gao:

            print(i, j)


