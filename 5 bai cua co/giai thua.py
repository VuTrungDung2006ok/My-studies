def giai_thua(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d
    
a, b = map(int, input().split())
c = map(int, input().split())
e = 0

for i in c:
    f = giai_thua(i)
    e += f
    
if e % giai_thua(b) == 0:
    print("YES")
else:
    print("NO")