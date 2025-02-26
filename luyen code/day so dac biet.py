n, k = map(int,input().split())
a = []
for i in range(1,n+1):
    if i %k ==0:
        a.append(i)

print(sum(a)) 