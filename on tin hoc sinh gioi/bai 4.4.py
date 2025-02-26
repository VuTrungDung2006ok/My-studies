def nguyento(x):
    if x ==2:
        return x
    if x < 2:
        return None
    if x > 2:
        for i in range(2,int(x**0.5)+1):
            if x% i == 0:
                return None
        return x
    
n, m = map(int,input().split())
b = []
for i in range(n, m+1):
    if nguyento(i) != None:
        b.append(i)

print(b)