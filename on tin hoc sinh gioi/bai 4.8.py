import math
n, m = map(int,input().split())
a = []
for i in range(n,m+1):
    for j in range(i+1,m+1):
        if math.gcd(i,j) == 1:
            a.append((i,j))

for k in a:
    print(k)



