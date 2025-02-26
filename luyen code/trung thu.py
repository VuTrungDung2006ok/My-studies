def tinhnhanh(x):
    s = (x*(x+1))//2
    return s

n , m = map(int,input().split())
d = 0
for i in range(1,n+1):
    if tinhnhanh(i) % m == 0:
        d+=1

print(d) 