n =int(input())
kq =[]
for i in range(n):
    a,b = map(int,input().split())
    e = a % 10
    if b == 0:
        kq.append(1)
    elif b % 4 != 0:
        z = (e**(b%4))%10
        kq.append(z)
    else:
        z = (e**4)%10
        kq.append(z)

for j in kq:
    print(j)