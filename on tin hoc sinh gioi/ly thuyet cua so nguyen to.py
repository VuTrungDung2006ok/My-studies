import math
n = int(input())
b = [1] * (n+1)

for i in range(2,n//2 +1):
    if b[i] == 1:
        for j in range(i*i, n+1, i):
            b[j] = 0

nt = [i for i in range(2,n+1) if b[i] == 1]
print(nt)