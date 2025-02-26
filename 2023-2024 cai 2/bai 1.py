l, r , a ,b = map(int,input().split())
d = 0
for i in range(l,r+1):
    if i % a == 0 or i % b == 0:
        d +=1

print(d)
