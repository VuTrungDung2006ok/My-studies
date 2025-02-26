n = int(input("viet so luong so"))
a = []
for i in range(0,n):
    a.append(int(input()))
    b = max(a)
    c = a.count(b)
for j in range(c):
    a.remove(b)
    d = max(a)

print(d)    

