n = int(input())
s = 0
d = 0
k = 0
for i in range(1,n+1):
    s +=i
    d +=1
    if s < n:
        k = d 
print(k)