t = int(input())
kq = []
for i in range(t):
    n = int(input())
    kq.append(bin(n))

for k in kq:
    print(k[2:])
