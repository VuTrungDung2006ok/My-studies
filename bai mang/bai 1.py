n = int(input("viet so luong so"))
a = []
b = []
for i in range(1,n+1):
    a.append(int(input()))

for j in a:
    b.append(a.count(j))

print(max(b))