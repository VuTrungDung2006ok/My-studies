m = int(input())
tich = 1
d = 0
while m > 0:
    tich *= m%10
    m = m //10
    d +=1

print(tich, d)