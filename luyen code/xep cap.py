m, n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a)
b = sorted(b)
d = 0
for i in a:
    for j in b:
        if i > j:
            d+=1
            b.remove(j)
            break
print(d)
    


