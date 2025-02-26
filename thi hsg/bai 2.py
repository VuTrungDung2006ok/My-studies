n , m = map(float,input().split())
a = list(map(float,input().split()))
b = []
for i in a:
    d = 0
    if i > m:
        d +=1
        b.append(d)

if len(b) >=2:
    print("DANGER")
else:
    print("SAFE")
    
        
    