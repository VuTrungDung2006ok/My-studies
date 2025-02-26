n = input()
a = []
for i in n:
    a.append(i)

tong = 0
for j in range(len(a)):
    tong += (int(a[j])**int(len(a)))

if tong == int(n):
    print(1)
else:
    print(0)
    
    