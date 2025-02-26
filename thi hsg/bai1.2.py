from math import ceil
n = int(input())
b = 0
c = 0

for i in range(0,n):
    b1,c1 = map(int,input().split())
    b += b1
    c += c1

print(ceil(c/b))
