a = input()
n =len(a)

d = 1
tong = ""
for i in range(1, n):
    if a[i] == a[i-1]:
        d +=1
    else:
        tong += str(d) +  a[i-1]
        d = 1

tong += str(d) + a[n-1]

print(tong)



