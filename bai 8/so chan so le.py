n = list(map(int,input().split()))
a =[]
b =[]
for i in n:
    if i % 2 ==0:
        a.append(i)
    elif i % 2!= 0:
        b.append(i)
c = a + [0] * n.count(0) + b

print(c)
    



