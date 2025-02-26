n , d = map(int,input().split())
a = list(map(int,input().split()))
b = []
kq = []
m = 0
for i in range(0,n):
    #xet tu a[i]
    b.clear()
    b.append(str(i+1))
    duoi = a[i]
    for j in range(i+1, n):
        if a[j] == duoi + d:
            duoi = a[j]
            b.append(str(j+1))
    if len(b) > m:
        m = len(b)
        kq = b.copy()

print(m)
print(" ".join(kq))
        

