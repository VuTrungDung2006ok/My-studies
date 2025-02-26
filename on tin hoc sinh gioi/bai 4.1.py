def nguyento(x):
    for i in range(2,int(x**1/2)+1):
        if x % i ==0:
            return "NO"
    return "YES"

n = int(input())
a = []
for i in range(n):
    m = int(input())
    a.append(nguyento(m))

for j in a:
    print(j)
