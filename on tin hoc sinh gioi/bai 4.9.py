def nguyento(x):
    if x < 2:
        return
    if x == 2:
        return x
    if x > 2:
        for i in range(2, int(x**0.5)+1):
            if x % i ==0:
                return
        return x

kq = []
so = int(input())
for i in range(so):
    a = [1]
    n = int(input())
    for j in range(2,n+1):
        if j % 2==0:
            a.append(2)
        elif nguyento(j) != None:
            a.append(j)
        else:
            a.append(3)

    kq.append(a)

for k in kq:
    print(" ".join(map(str, k)))
    ## Chuyển các phần tử thành chuỗi và nối với dấu cách
    #" ".join(...) nối các chuỗi lại với nhau, với dấu cách (" ") làm phân cách giữa các phần tử.

