def giaithua(x):
    d = 1
    for i in range(1,x+1):
        d *= i
        
    return d

h = 0
n = list(map(int,input().split()))
for j in range(1,n[1]+1):
    e = 1 + (n[0]**(2*j)) / (giaithua(j))
    h = e+ e
print(h)
    