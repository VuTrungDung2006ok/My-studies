so = int(input())
a = []
kq = []
for i in range(so):
    n = int(input())
    a.append((((5*n*n)+4),((5*n*n)-4)))

for j in a:
    if (int(j[0]**0.5))**2 == j[0] or (int(j[1]**0.5))**2 == j[1]:
        kq.append("YES")
    else:
        kq.append("NO")

for k in kq:
    print(k)

