n = list(map(int,input().split()))
while len(n) >2 and n[1] > n[0]:
    n = list(map(int,input().split()))
d = 0
for i in range(n[1],n[0]):
    p = i ** 2
    if p < n[0]:
        d+=1
        
print(d)