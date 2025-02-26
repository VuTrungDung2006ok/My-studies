import math
def nguyento(x):
    if x < 2:
        return "NO"
    if x > 2:
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                return "NO"
        return x
    if x == 2:
        return x
    

n = int(input())
a = list(map(int,input().split()))
b = []
for j in a:
    if nguyento(j) == j:
        b.append(j)
# dang sai phan lap lai so
c = sorted(list(set(b))) # set la code xoa phan tu lap trong chuoi
for k in c:
    print(k, end=" ")



        

