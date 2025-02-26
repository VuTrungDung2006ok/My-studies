n = int(input())
istr = str(n)
chan = 0
le = 0
while n < 0:
    print("vui long nhap lai")
    n = int(input())

if n > 0 :
    for i in istr:
        i = int(i)
        if i % 2 ==0:
            chan +=1
        else:
            le +=1
        
print(chan, le)
