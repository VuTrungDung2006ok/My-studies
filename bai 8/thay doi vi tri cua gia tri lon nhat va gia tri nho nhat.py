a = list(map(int,input().split()))
for i in a:
    b = a.index(max(a))
    c = a.index(min(a))
    a[c] , a[b] = a[b] , a[c] 

print(a)
