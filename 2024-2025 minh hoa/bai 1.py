k,a,b = map(int,input().split())
tich = 0
d = 0

for i in range(1,k+1):
    for j in range(i,k+1):
        for l in range(j,k+1):
            tich = i * j * l
            if a <= tich <= b:
                d+=1

print(d)
