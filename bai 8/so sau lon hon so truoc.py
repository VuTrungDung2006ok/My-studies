a = list(map(int,input().split()))
d = 0
for i in a:
    b = max(a)
    d+=1
    a.remove(b)
    
print(d)